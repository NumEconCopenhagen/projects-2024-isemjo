from types import SimpleNamespace
import numpy as np
from scipy import optimize
import pandas as pd 
import matplotlib.pyplot as plt
import warnings
from scipy.optimize import minimize

class ExchangeEconomyClass:

    def __init__(self):

        par = self.par = SimpleNamespace()

        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3

        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3

        par.w1B = 1- par.w1A
        par.w2B = 1- par.w2A

    def utility_A(self,x1A,x2A):
        par=self.par
        return x1A**par.alpha *x2A**(1-par.alpha)


    def utility_B(self,x1B,x2B):
        par=self.par
        return x1B**par.beta *x2B**(1-par.beta)

    def demand_A(self,p1):
        par=self.par
        return par.alpha*(p1*par.w1A+par.w2A)/p1,(1-par.alpha) *(p1*par.w1A+par.w2A)

    def demand_B(self,p1):
        par=self.par
        return par.beta*(p1*par.w1B+par.w2B)/p1, (1-par.beta) *(p1*par.w1B+par.w2B)

    def check_market_clearing(self,p1):

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2
    
    