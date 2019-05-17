# -*- coding: utf-8 -*-

"""
Created on Mon Jun 16 15:54:46 2014
EDIT VARIABLE imax TO CHANGE THE BIN AREA.
@author: severo
"""

from scipy import *
import scipy.optimize
from scipy.integrate import quad
from math import *
import numpy as np


# Bissection method with long double precision
def fsolve(f, a, b, xtol=1e-18):
    """ fsolve(f, fprime, x0, xtol=1e-18) -> x: f(x) = 0; implemented to longdouble precision
    Uses Secant Method, requires a <= x < b there are no safeguards with this implementation.
    """
    assert a < b, "a must be lower bound, b must be higher bound"
    x = [b, a]
    F = list(map(f, x))
    for n in range(2, 100):
        x.append(x[n-1] - F[n-1]*(x[n-1] - x[n-2])/(F[n-1] - F[n-2]))
        if abs(x[n] - x[n-1]) < xtol: 
            return x[n]
        F.append(f(x[n]))
    return 0

# redefine Transcendental functions for proper precision
exp = lambda x: np.exp(x, dtype=np.longdouble)
sqrt = lambda x: np.sqrt(x, dtype=np.longdouble)
power = lambda x, y: np.power(x, y, dtype=np.longdouble)

oneHalf = 1/np.longdouble(2)

# Define parameters
imax=longdouble(8)
area=1/longdouble(imax)

# Wanted distribution
P = lambda x: (2/sqrt(2*pi))*exp(-x*x*oneHalf)

# Solve for X and Y
X=[fsolve(lambda x: x*P(x)-area,1,4)]
Y=[P(X[0])]
A=[1-erf(X[0]/sqrt(2))]

while X[-1] > 0:
    X.append(fsolve(lambda x: x*(P(x) - Y[-1]) - area, X[-1]*oneHalf, X[-1]))
    Y.append(P(X[-1]))
    A.append(erf(X[-2]/sqrt(2))-erf(X[-1]/sqrt(2))-(X[-2]-X[-1])*P(X[-2]))
        
    
X=X[0:-1]
Y=Y[0:-1]

# Calculate cap area
A[-1]=erf(X[-1]/sqrt(2))-X[-1]*P(X[-1])

print("Chosen area size was 1/{}").format(imax)
print("Lmax is {0}, boxes cover Lmax*area={1} of the region under the curve").format(len(X),len(X)*area)
print("Ziggurat lengths stored in X")
print("Ziggurat heights stored in Y")
print("Area of left over regions stored in A (first element is the tail, last one is the cap)")

# Plot
x=linspace(0,ceil(X[0]),1000)
plot(x,P(x))
scatter(X,Y)

plot([0, X[0]], [Y[0], Y[0]], 'k-', lw=1)
plot([X[0], X[0]], [0, Y[0]], 'k-', lw=1)
plot([0, X[0]], [0, 0], 'k-', lw=1)
for i in range(len(X)-1):
    i=i+1
    plot([0, X[i]], [Y[i], Y[i]], 'k-', lw=1)
    plot([X[i], X[i]], [Y[i], Y[i-1]], 'k-', lw=1)
