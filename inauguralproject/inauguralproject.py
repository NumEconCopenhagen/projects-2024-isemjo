from types import SimpleNamespace
import numpy as np
from scipy import optimize
import pandas as pd 
import matplotlib.pyplot as plt
import warnings

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

        u=x1A**par.alpha *x2A**(1-par.alpha)
        return u 

    def utility_B(self,x1B,x2B):
        par=self.par

        u=x1B**par.beta *x2B**(1-par.beta)
        return u 

    def demand_A(self,p1):
        par=self.par

        x1A = par.alpha*(p1*par.w1A+par.w2A)/p1
        x2A = (1-par.alpha) *(p1*par.w1A+par.w2A)
        return x1A, x2A

    def demand_B(self,p1):
        par=self.par

        x1B = par.beta*(p1*par.w1B+par.w2B)/p1
        x2B = (1-par.beta) *(p1*par.w1B+par.w2B)
        return x1B, x2B

    def check_market_clearing(self,p1):

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        x1A + x1B == par.w1A + par.w1B

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2
    
    def Edgeworth_box_C(x1A, x2A)
        par = self.par

        

        