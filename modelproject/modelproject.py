import numpy as np
from scipy import optimize
import random

#This function defines the Solow growth model equation that will be solved for the steady state (SS) of the capital-output ratio, z
def solow_equation(variable, s, n, g, delta, alpha, beta, kappa):
    """
    Args:
        variables (list or tuple): Contains one variables to be solved for: capital output ratio
        s               (float): Savings rate
        n                 (float): Population growth rate
        g                 (float): TFP growth rate
        delta             (float): Depreciation rate
        alpha             (float): Output elasticity of capital
        beta              (float): Output elasticity of labor 
        kappa             (float): Output elasticity of land
    Returns:
        Solow equation for z_{t+1}-z_{t}
    """
    # Variables to be solved for: capital output ratio
    z = variable
    
    # Checks if the variable, z is less than or equal to zero
    if z <= 0:
        # Returning a very large residual if true. 
        #This check prevents the function form evaluating non-positive values of z which would be economically meaningless.
        return [np.inf]

    # Set Solow equation for z_{t+1}-z_{t} = 0
    solow_z = (1 / ((1 + n) * (1 + g)))**beta * (s + (1 - delta) * z)**(1 - alpha) * z**alpha - z
    # Return equations
    return solow_z

#This function defines a multi-start optimization to find the SS solution, z* of the Solow model by using multiple initial guesses. 
def multi_start(num_guesses=100, bounds=[1e-5, 50], fun=solow_equation, args= None, method='hybr'):
    """
    Performs multi-start optimization to find the steady state solution for z.
    
    Args:
        num_guesses     (int): The number of random initial guesses
        bounds        (tuple): Range within which these initial guesses are generated
        fun        (function): The function to be optimized
        args          (tuple): The tuple of arguments for the function
        method       (method): The optimization method to used; "hypr" refers to a hybrid methoed combining several algorithms
    
    Returns:
        The steady state values for z and the residual of the function
    """
    # Initializes the smallest residual as infinity to track the best solution found during the optimization. 
    smallest_residual = np.inf

    # Generates a list of random values within the specified bounds to serve as initial guesses-
    random_samples = list(np.random.uniform(low=bounds[0], high=bounds[1], size=num_guesses))

    # Creating a loop through each random initial guess
    for i in range(num_guesses):
        # For the initial guess will a random pair of numbers from the list of random samples be selected.
        initial_guess = random.sample(random_samples, 1)

        # The optimization problem is soleved with the current initial guess
        sol = optimize.root(fun = fun, x0 = initial_guess, args = args, method = method)
        
        # For each solution the residual norm (Euclidean norm) is calculated.
        residual_norm = np.linalg.norm(sol.fun)

        # The best solution is found: If the residual norm is smaller than the current smallest residual, update the steady state of z and the smallest residual
        if residual_norm < smallest_residual:
            smallest_residual = residual_norm
            steady_state_z = sol.x
    
    # Return optimal solutions 
    return steady_state_z, smallest_residual

#This function defines the Solow growth model equation that will be solved for the steady state (SS) of the capital-output ratio, j
def solow_equation1(variable, s, n, g, delta, alpha, beta, kappa, epsilon, psi):
    """
    Args:
        variables (list or tuple): Contains one variables to be solved for: capital output ratio
        s                 (float): Savings rate
        n                 (float): Population growth rate
        g                 (float): TFP growth rate
        delta             (float): Depreciation rate
        psi               (float): Consumption of natural ressource rate
        alpha             (float): Output elasticity of capital
        beta              (float): Output elasticity of labor 
        kappa             (float): Output elasticity of land
        epsilon           (float): Output elasticity of exhastible natural resources
    Returns:
        Solow equation for j_{t+1}-j_{t}
    """
    # Variables to be solved for: capital output ratio
    j = variable
    
    # Checks if the variable, z is less than or equal to zero
    if j <= 0:
        # Returning a very large residual if true. 
        #This check prevents the function form evaluating non-positive values of z which would be economically meaningless.
        return [np.inf]

    # Set Solow equation for z_{t+1}-z_{t} = 0
    solow_j = (1 / (((1 + n) * (1 + g)))**beta *(1-psi)**epsilon)* (s + (1 - delta) * j)**(1 - alpha) * j**alpha - j
    # Return equations
    return solow_j

#This function defines a multi-start optimization to find the SS solution, j* of the Solow model by using multiple initial guesses. 
def multi_start1(num_guesses=100, bounds=[1e-5, 50], fun=solow_equation1, args= None, method='hybr'):
    """
    Performs multi-start1 optimization to find the steady state solution for j.
    
    Args:
        num_guesses     (int): The number of random initial guesses
        bounds        (tuple): Range within which these initial guesses are generated
        fun        (function): The function to be optimized
        args          (tuple): The tuple of arguments for the function
        method       (method): The optimization method to used; "hypr" refers to a hybrid methoed combining several algorithms
    
    Returns:
        The steady state values for j and the residual of the function
    """
    # Initializes the smallest residual as infinity to track the best solution found during the optimization. 
    smallest_residual = np.inf

    # Generates a list of random values within the specified bounds to serve as initial guesses-
    random_samples = list(np.random.uniform(low=bounds[0], high=bounds[1], size=num_guesses))

    # Creating a loop through each random initial guess
    for i in range(num_guesses):
        # For the initial guess will a random pair of numbers from the list of random samples be selected.
        initial_guess = random.sample(random_samples, 1)

        # The optimization problem is soleved with the current initial guess
        sol = optimize.root(fun = fun, x0 = initial_guess, args = args, method = method)
        
        # For each solution the residual norm (Euclidean norm) is calculated.
        residual_norm = np.linalg.norm(sol.fun)

        # The best solution is found: If the residual norm is smaller than the current smallest residual, update the steady state of j and the smallest residual
        if residual_norm < smallest_residual:
            smallest_residual = residual_norm
            steady_state_j = sol.x
    
    # Return optimal solutions 
    return steady_state_j, smallest_residual

