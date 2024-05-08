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

