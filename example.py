from src import MonteCarloIntegrator
import numpy as np
def f(x): 
    return np.linalg.norm(np.array(x))**2

integrator = MonteCarloIntegrator(1000000)

print(integrator.integrate(f=f, lower_bound=[-2, -2], upper_bound=[2,2], dimensions=2))
