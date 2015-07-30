#! /usr/bin/python

from math import *
import numpy as np

np.set_printoptions(precision=6) ## control numpy's decimal output :)

form = raw_input('Enter the function of u & t only >> ')
start = input("Enter the lower limit of the interval >> ")
stop = input("Enter the upper limit of the interval >> ")
h = input("Using step size? ")

t = np.arange(start, stop + h, h)

N = int((stop - start)/ h)  ##calculate the number of times to iterate
u = np.zeros(N +1,)     ## fill our u's first with  N+1 0's

k1 = np.zeros((N,1) )
k2 = np.zeros((N,1) )
u[0] = 1   ## initial conditions

def step_sizes():
    print t  ##call step_sizes() if you need the mesh points

def f(t, u):
    return eval(form) ## define the user's function
    
def answers():
    for j in range(0, N): ## do for N times
        k1 = h *f(t[j], u[j])
        k2 = h * f(t[j]+0.5*h , u[j] + (k1 /2))
        c, d = k1, float('%.11f'% k2) ## keep rounded off to decimal places
        u[j+1] = u[j] + d 
    return u

def kone():
    for j in range(0, N): ## do for N times
        k1[j] = h *f(t[j], u[j])
        k2[j] = h * f(t[j]+0.5*h , u[j] + (k1[j] /2))
    return k1

def ktwo():
    for j in range(0, N): ## do for N times
        k1[j] = h *f(t[j], u[j])
        k2[j] = h * f(t[j]+0.5*h , u[j] + (k1[j] /2))
    return k2

def exact_solution(): 
    return 1/(1 + t**2) ## call exact_solution to print exact solutions 

values = np.delete(answers(), u[1])
evalues = np.delete(exact_solution(), t[0])
errors = abs(values - evalues)

print "\r\n k1 = ", kone(), "\r\n k2 = ", ktwo(),'\r\n'
print "The results for the iterations are\r\n u_j ~ ",  values,  "for",  N, "intervals \r\n exact values are ",  evalues

