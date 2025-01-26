import pandas as pd
import linopy as lp

# data
df_gen = pd.read_csv('scripts/linopy/data/df_gen.csv').set_index('generator')
df_load = pd.read_csv('scripts/linopy/data/df_load.csv').set_index('time')*3
# formulation
m = lp.Model()
# Variable (constants)
generation = m.add_variables(
    lower=0, upper=df_gen['p_max'], coords=[df_gen.index, df_load.index], dims=['generator', 'time'], name='generation')
load = m.add_variables(
    lower=df_load['load_mw'], upper=df_load['load_mw'], coords=[df_load.index], dims=['time'], name='load')
marginal_cost = m.add_variables(
    lower=df_gen['marginal_cost'], upper=df_gen['marginal_cost'], coords=[df_gen.index], dims=['generator'], name='marginal_cost')

# Add slack variables for unserved energy (USE) and overgeneration (OG) per node
use = m.add_variables(lower=0, dims=['time'], coords=[df_load.index], name='use')
dump = m.add_variables(lower=0, dims=['time', 'generator'], coords=[df_load.index, df_gen.index], name="dump")

# Assign high penalty costs to discourage deviations
penalty_use = 29
penalty_dump = 10_000

# Constrain
power_balance = generation.sum(dim='generator') + dump.sum(dim='generator') == load - use
m.add_constraints(power_balance)

# Objective function: Minimize generation cost
objective_linear_expression = (marginal_cost * generation).sum() + (penalty_dump * dump).sum() + (penalty_use * use).sum()
m.add_objective(objective_linear_expression, sense='min')

m.solve(solver_name='highs')
# solutions
df_sol = m.solution.to_dataframe()
df_sol.to_csv('scripts/linopy/data/df_sol.csv')
df_pivot = df_sol.reset_index().pivot(index="time", columns="generator", values="generation").sort_index()
df_pivot['load']  = df_sol.reset_index()[['time', 'load']].drop_duplicates().groupby('time').sum()
df_cost = df_sol.reset_index()[['time', 'marginal_cost']].drop_duplicates().groupby('time').sum()
df_use = df_sol.reset_index()[['time', 'use']].drop_duplicates().groupby('time').sum()
df_dump = df_sol.reset_index()[['time', 'dump']].drop_duplicates().groupby('time').sum()

df_results = df_pivot
df_results['marginal_cost'] = df_cost['marginal_cost']
df_results['use'] = df_use['use']
df_results['dump']= df_dump['dump']