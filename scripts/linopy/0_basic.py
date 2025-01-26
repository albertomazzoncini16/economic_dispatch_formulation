import linopy as lp
import pandas as pd

m = lp.Model()
# basic variables:
# x = m.add_variables(lower=0, name="x")
# y = m.add_variables(lower=0, name="y")

# 1-coordinate (time) dependent variables - linopy automatically creates optimization variables for all coordinates:
time = pd.Index([f't_{x}' for x in range(24)], name="time")
x_quantity = m.add_variables(lower=0, coords=[time], name="x_quantity")
y_quantity = m.add_variables(lower=0, coords=[time], name="y_quantity")

# multiply the rhs with t. Note that the coordinates from the lhs and the rhs have to match.
# m.add_constraints(3 * x + 7 * y == 10)
# m.add_constraints(5 * x + 2 * y >= 3)
# 5 * x + 2 * y >= 3 this is a linopy.constraints.Constraint - unassigned
x_max_hourly = [10, 10, 10, 10, 98, 97, 23, 11, 75, 62, 76, 33, 85, 46, 5, 59, 43, 10, 10, 10, 10, 10, 10, 10]
y_max_hourly = [0, 0, 0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0]
facility_max_hourly_production = [20, 20, 20, 20, 196, 194, 46, 22, 150, 124, 152, 66, 170, 92, 10, 118, 86, 20, 20, 20, 20, 20, 20, 20]

factor_x_max_hourly = pd.Series(data=x_max_hourly, index=time)
factor_y_max_hourly = pd.Series(data=y_max_hourly, index=time)
factor_facility_max_hourly_production = pd.Series(data=facility_max_hourly_production, index=time)

con_x_max_hourly = m.add_constraints(x_quantity <= 1 * factor_x_max_hourly, name="con_x_max_hourly") # - assigned
con_y_max_hourly = m.add_constraints(y_quantity <= 1 * factor_y_max_hourly, name="con_y_max_hourly")
con_facility_max_hourly_production = m.add_constraints(y_quantity + x_quantity <= 1 * factor_facility_max_hourly_production, name="con_facility_max_hourly_production", coords=time)


# con1 = m.add_constraints(y >= 1 * factor_1, name="con1", coords=factor_1.index) # - assigned
# con2 = m.add_constraints(x >= 1 * factor_2, name="con2", coords=factor_1.index)
# when it comes to the objective, we use the sum function of linopy.LinearExpression.
# This stacks all terms of the time dimension and writes them into one big expression.
#basic obj = m.add_objective(x + 2 * y)
# x + 2 * y this is a linopy.expressions.LinearExpression
x_price = 3
y_price = 3.3
objective_linear_expression = x_price * x_quantity + y_price * y_quantity # x + y_exp is a linopy.expressions.LinearExpression

# Summation over dimensions
objective_function = objective_linear_expression.sum() # or (x + y_exp).sum() == (x + 2*y).sum()
m.add_objective(objective_function, sense='max')

m.solve(solver_name='highs')

df_sol = m.solution.to_dataframe()
print(df_sol.head(12))