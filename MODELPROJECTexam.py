from types import SimpleNamespace
import numpy as np
from scipy import optimize
import random
import matplotlib.pyplot as plt


class Solowmodelkap7:
    # 0. Defining the initiation function  
    def __init__(self):
    
        par = self.par = SimpleNamespace ()
        sol = self.sol = SimpleNamespace ()

        # Defining parameters from H. J. Whitta-Jacobsen and P. B. Sørensen which is based on approximate empirical data.
        par.s_val = 0.2
        par.n_val = 0.005
        par.g_val = 0.02
        par.delta_val = 0.06
        par.alpha_val = 0.2
        par.beta_val = 0.6
        par.kappa_val = 0.2
        par.X_val = 100

        # Parameters for the extended model in section 2.
        par.psi_val = 0.05
        par.epsilon_val = 0.1

        # c. Parameters for the simulation in section 1.4
        par.k0 = 1
        par.a0 = 1
        par.l0 = 1
        par.t0 = 0
        par.T = 300
    
        # d. Arrays for the simulation in section 1.4
        # i. Arrays to hold values for baseline estimation
        sol.z = np.zeros(par.T+1) # output-capital ratio
        sol.k = np.zeros(par.T+1) # Capital
        sol.y = np.zeros(par.T+1) # Output
        sol.l = np.zeros(par.T+1) # Workers
        sol.a = np.zeros(par.T+1) # Technology
        sol.x = np.zeros(par.T+1) # Land
        sol.yG = [] # Growth in output

        # ii. Defining the time array
        sol.t = np.arange(par.T)

    # 2. This function defines the Solow growth model equation that will be solved for the steady state (SS) of the capital-output ratio, z
    def trans_equation(self, z):
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
        
            par = self.par
        
            # Set Solow equation for z_{t+1}-z_{t} = 0
            trans_z = (1 / ((1 + par.n_val) * (1 + par.g_val)))**par.beta_val * (par.s_val + (1 - par.delta_val) * z)**(1 - par.alpha_val) * z**par.alpha_val - z
            # Return equations
            return trans_z

    # 3. Solving SS numerically
    def multi_hybr(self, num_guesses=100, bounds=[1e-5, 50], args= None, method='hybr'):
        """
        Performs multi-hypr optimization to find the steady state solution for z.
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
            result = optimize.root(fun=self.trans_equation, x0 = initial_guess, method = method)
            
            # For each solution the residual norm (Euclidean norm) is calculated.
            residual_norm = np.linalg.norm(result.fun)

            # The best solution is found: If the residual norm is smaller than the current smallest residual, update the steady state of z and the smallest residual
            if residual_norm < smallest_residual:
                smallest_residual = residual_norm
                steady_state_z = result.x
        
        # Return optimal solutions 
        return steady_state_z, smallest_residual

    # 4. Simulation with interactive shock 
    def X_shock(self, shock):
    
        """
        This function simulates the model with an interactive shock to X
        The function returns a plot of the simulation
        """ 
        
        par = self.par
        sol = self.sol 

        sol.k[0] = par.k0
        sol.a[0] = par.a0
        sol.l[0] = par.l0
        sol.yG = []

        # b. Simulating and creating shock in period 2 and onwards
        for i in range(par.T):
            # i. Setting X to "100-150" in period 100
            if i >= 100:
              par.X_val = shock   
            
            # iii. The equations that make up the model
            sol.z[i+1] = sol.y[i+1]/sol.k[i+1]
            sol.y[i+1] = sol.k[i]**par.alpha_val * par.X_val**par.kappa_val * (sol.a[i]*sol.l[i])**(par.beta_val)
            sol.l[i+1] = (1+par.n_val) * sol.l[i]
            sol.a[i+1] = (1+par.g_val) * sol.a[i]
            sol.k[i+1] = par.s_val * sol.y[i] + (1-par.delta_val) * sol.k[i]
            
            # iv. Calculating the growth in y and appending to list, if it hits a 0 we set it to 0.00001
            sol.yG.append(np.log(sol.y[i+1] if sol.y[i+1] != 0 else 0.00001) - np.log(sol.y[i] if sol.y[i] != 0 else 0.00001))

        # c. Creating plot
        fig = plt.figure(figsize=(13,5))
        ax = fig.add_subplot(1,2,1)

        # d. Plotting the simulation
        ax.plot(sol.yG[2:], color="blue", label="Land")
        plt.axhline(sol.yG[249],xmax=1,color="black",linestyle="--")
        plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))

        # e. Setting labels and title
        ax.set_ylabel('Growth in y')
        ax.set_xlabel('Time')
        ax.set_title('Growth in y, solow model with land')
        ax.set_xlim(-2, 250)
        ax.grid(True)

        plt.show()

    # 5. This function defines the Solow growth model extend with natural resources equation that will be solved for the steady state (SS) of the capital-output ratio, j
    def trans_equation1(self, j):
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
            par = self.par
       
            # Set Solow equation for z_{t+1}-z_{t} = 0
            trans_j = (1 / (((1 + par.n_val) * (1 + par.g_val)))**par.beta_val *(1-par.psi_val)**par.epsilon_val)* (par.s_val + (1 - par.delta_val) * j)**(1 - par.alpha_val) * j**par.alpha_val - j
            # Return equations
            return trans_j
    
   # 6. This function defines a multi-hybr optimization to find the SS solution, j* of the Solow model by using multiple initial guesses. 
    def multi_hybr1(self, num_guesses=100, bounds=[1e-5, 50], args= None, method='hybr'):
        """
        Performs multi-hybr1 optimization to find the steady state solution for j.
        
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
        smallest_residual1 = np.inf

        # Generates a list of random values within the specified bounds to serve as initial guesses-
        random_samples = list(np.random.uniform(low=bounds[0], high=bounds[1], size=num_guesses))

        # Creating a loop through each random initial guess
        for i in range(num_guesses):
            # For the initial guess will a random pair of numbers from the list of random samples be selected.
            initial_guess = random.sample(random_samples, 1)

            # The optimization problem is soleved with the current initial guess
            result1 = optimize.root(fun = self.trans_equation1, x0 = initial_guess, method = method)
            
            # For each solution the residual norm (Euclidean norm) is calculated.
            residual_norm = np.linalg.norm(result1.fun)

            # The best solution is found: If the residual norm is smaller than the current smallest residual, update the steady state of j and the smallest residual
            if residual_norm < smallest_residual1:
                smallest_residual1 = residual_norm
                steady_state_j = result1.x
        
        # Return optimal solutions 
        return steady_state_j, smallest_residual1


