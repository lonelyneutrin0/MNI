# A simple one dimensional test case to demonstrate feasibility 
import numpy as np 
from dataclasses import dataclass
import inspect
from typing import Callable

@dataclass
class MonteCarloIntegrator: 
    samples: int
    """ 
    A class representing the Monte Carlo Integrator object 
    :param samples: The number of points to sample from the domain- higher values improve accuracy
    """
    def integrate(self, f:Callable[[list], float], lower_bound:list[float], upper_bound:list[float], dimensions:int,  p=None): 
        """ 
        The Monte Carlo Integrator 
        :param f: The function to integrate 
        :param lower_bound: A list containing the lower bound for each variable 
        :param upper_bound: A list containing the upper bound for each variable  
        :param dimensions: The dimensionality of the function domain 
        :param p: The probability function for importance sampling. Defaults to None 
        """
        
        # Make sure the bounds are of the right dimensionality 
        if(len(lower_bound) != len(upper_bound) or len(lower_bound) != dimensions): raise ValueError(f'Improper dimensionality')
        
        # Convert the bounds to numpy arrays 
        lower_bound = np.array(lower_bound)
        upper_bound = np.array(upper_bound)
        
        # Produce a matrix of points to sample from
        value_grid = np.random.uniform(low=lower_bound[:, None], high=upper_bound[:, None], size=(dimensions, self.samples))
        
        sum = 0
        if p is None: 
            for i in range(self.samples): 
                sum+= f(value_grid[:, i].tolist())
            return np.prod(upper_bound-lower_bound)*sum/self.samples
        
        for i in range(self.samples): 
            sum+= f(value_grid[:, i].tolist())/p(value_grid[:, i].tolist())
        return sum/self.samples