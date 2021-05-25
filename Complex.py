"""
Input a complex number and print the values of its r and phase
"""

from cmath import phase

inp = '1+2j'
comp = complex(inp)

print("r = {}".format(abs(comp)))
print("phase = {}".format(phase(comp)))
