# A simple one dimensional test case to demonstrate feasibility 
import numpy as np 
from dataclasses import dataclass
import inspect

@dataclass
class MonteCarloIntegrator: 
    samples: int
    """ 
    A class representing the Monte Carlo Integrator object 
    :param samples: The number of points to sample from the domain- higher values improve accuracy
    """
    def integrate(self, f, lower_bound:np.ndarray, upper_bound:np.ndarray,  p=None): 
        """ 
        The function to optimize the 
        """
        # Determine the number of dimensions
        num_dimensions = len(inspect.signature(f).parameters)
        # Make sure the bounds are of the right dimensionality 
        if(lower_bound.shape != upper_bound.shape): raise ValueError("Dimensionality mismatch of bounds")
        if(lower_bound.size != num_dimensions): raise ValueError("Dimensionality mismatch")
        
        value_grid = np.zeros((num_dimensions,self.samples))
        value_grid = np.random.uniform(low=lower_bound[:, None], high=upper_bound[:, None], size=(num_dimensions, self.samples))
        
        sum = 0
        if p is None: 
            for i in range(self.samples): 
                sum+= f(*value_grid[:, i])
            return np.prod(upper_bound-lower_bound)*sum/self.samples
        
        for i in range(self.samples): 
            sum+= f(*value_grid[:, i])/p(*value_grid[:, i])
        return sum/self.samples