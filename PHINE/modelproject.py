import numpy as np
from scipy import optimize
import random

def solow_equations(variables, s, n, g, delta, alpha):
    """
    Args:
        variables (list or tuple): Contains two variables to be solved for: physical capital and human capital
        s               (float): Savings rate in capital
        n                 (float): Population growth rate
        g                 (float): TFP growth rate
        delta             (float): Depreciation rate
        alpha             (float): Output elasticity of physical capital
    
    Returns:
        Solow equations for k_{t+1}-k_{t} = 0  
    """
    # Variables to be solved for:  capital 
    k = variables
    
    # Checks for edge cases, used in multi_start
    if k <= 0:
        # Return a very large residual to indicate a poor solution
        return [np.inf, np.inf]

    # Set Solow equations for k_{t+1}-k_{t} = 0 
    solow_k = (1 / ((1 + n) * (1 + g))) * (s * k**alpha + (1-delta) * k)
     
    # Return equations
    return solow_k

def multi_start(num_guesses=100, bounds=[1e-5, 50], fun=solow_equations, args= None, method='hybr'):
    """
    Performs multi-start optimization to find the steady state solutions for k.
    
    Args:
        num_guesses     (int): The number of random initial guesses, default = 100
        bounds        (tuple): The bounds for the random initial guesses, default = [1e-5, 50]
        fun        (function): The function to be optimized, default = n_ss_solow
        args          (tuple): The tuple of arguments for the function, default = None
        method       (method): The optimization method to use, default = 'hybr'
    
    Returns:
        The steady state values for k and y, and the residual of the function
    """
    # Initialize the smallest residual as infinity
    smallest_residual = np.inf

    # Generate a list of random numbers within the specified bounds
    random_samples = list(np.random.uniform(low=bounds[0], high=bounds[1], size=num_guesses))



    # Loop through each random initial guess
    for i in range(num_guesses):
        # Select a random pair of numbers from the list of random samples
        initial_guess = random.sample(random_samples, 2)

        # Solve the optimization problem with the current initial guess
        sol = optimize.root(fun = fun, x0 = initial_guess, args = args, method = method)
        
        # Calculate the residual norm (Euclidean norm) of the current solution
        residual_norm = np.linalg.norm(sol.fun)

        # If the residual norm is smaller than the current smallest residual, update the steady state of k and h and the smallest residual
        if residual_norm < smallest_residual:
            smallest_residual = residual_norm
            steady_state_k = sol.x
    
    # Return optimal solutions 
    return steady_state_k, smallest_residual