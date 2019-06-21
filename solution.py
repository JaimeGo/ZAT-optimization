from scipy.optimize import minimize
import numpy as np

# Initial guess
x0=[0]

# Objective function
def objective(x):
    return x[0]

#Constraints
def constraint1(x):
    return x[0]

def constraint2(x):
    return x[0]

con1={'type':'ineq','fun':constraint1}
con2={'type':'ineq','fun':constraint2}

cons=[con1,con2]

# Bounds
bnds=((1,1),(1,1))

# Minimization function
res = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)

print(res.x)