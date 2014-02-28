# This program implements a solution for the 120th Project Euler Problem

from math import pow

def modSquare(a, n):
    return (pow(a-1, n) + pow(a+1, n))%a**2
    
