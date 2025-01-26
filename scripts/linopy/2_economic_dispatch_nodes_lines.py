import pandas as pd
import linopy as lp

# data
df_gen = pd.read_csv('scripts/linopy/data/df_gen.csv').set_index('generator')
df_load = pd.read_csv('scripts/linopy/data/df_load.csv').set_index('time')
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