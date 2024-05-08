import numpy as np
from scipy import optimize
import random

def solow_equation(variable, s, n, g, delta, alpha, beta):
    """
    Args:
        variables (list or tuple): Contains one variables to be solved for: physical capital
        s               (float): Savings rate
        n                 (float): Population growth rate
        g                 (float): TFP growth rate
        delta             (float): Depreciation rate
        alpha             (float): Output elasticity of physical capital
        beta              (float): Output elasticity of labor-augmenting productivity
    Returns:
        Solow equation for z_{t+1}-z_{t}
    """
    # Variables to be solved for: capital output ratio
    z = variable
    
    # Checks for edge cases, used in multi_start
    if z <= 0:
        # Return a very large residual to indicate a poor solution
        return [np.inf, np.inf]

    # Set Solow equation for z_{t+1}-z_{t} = 0
    solow_z = (1 / ((1 + n) * (1 + g)))**beta * (s + (1 - delta) * z)**(1 - alpha) * z**alpha - z
    # Return equations
    return solow_z


def multi_start(num_guesses=100, bounds=[1e-5, 50], fun=solow_equation, args= None, method='hybr'):
    """
    Performs multi-start optimization to find the steady state solution for z.
    
    Args:
        num_guesses     (int): The number of random initial guesses, default = 100
        bounds        (tuple): The bounds for the random initial guesses, default = [1e-5, 50]
        fun        (function): The function to be optimized, default = n_ss_solow
        args          (tuple): The tuple of arguments for the function, default = None
        method       (method): The optimization method to use, default = 'hybr'
    
    Returns:
        The steady state values for z and the residual of the function
    """
    # Initialize the smallest residual as infinity
    smallest_residual = np.inf

    # Generate a list of random numbers within the specified bounds
    random_samples = list(np.random.uniform(low=bounds[0], high=bounds[1], size=num_guesses))

    # Loop through each random initial guess
    for i in range(num_guesses):
        # Select a random pair of numbers from the list of random samples
        initial_guess = random.sample(random_samples, 1)

        # Solve the optimization problem with the current initial guess
        sol = optimize.root(fun = fun, x0 = initial_guess, args = args, method = method)
        
        # Calculate the residual norm (Euclidean norm) of the current solution
        residual_norm = np.linalg.norm(sol.fun)

        # If the residual norm is smaller than the current smallest residual, update the steady state of z and the smallest residual
        if residual_norm < smallest_residual:
            smallest_residual = residual_norm
            steady_state_z = sol.x
    
    # Return optimal solutions 
    return steady_state_z, smallest_residual

