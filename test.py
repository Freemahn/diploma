from sympy import *
import sympy
import random
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve
from lib import *

init_printing()

a, b, c, d,d1,d2 = symbols('a, b, c, d, d1, d2')
a1, b1, c1 = symbols('a1, b1, c1')
m, L, H0 = symbols('m, L, H0')
x, y = symbols('x, y')
v0, v1 = symbols('v0, v1')
# d1, d2 = symbols('d1, d2')
H0_, L_ = 1, 10
m_ = 1
H = H0_ - (x - L_ / 2) ** 2
vx = (v0 + a * x * (x - L_)) * (y ** 2 - H ** 2)
dxvx = diff(vx, x)
dyvy = - dxvx
print("dyvy=", dyvy)
print('='*50)
vy = integrate(dyvy, y)
vy = substitute(vy, [a, v0], [a1, v1])

# vx = substitute(vx, [L, H0], [L_, H0_])
# vy = substitute(vy, [L, H0], [L_, H0_])
print("vx=", vx)
pprint(vx)
print('- '*100)
print("vy=", vy)
pprint(vy)
print('='*100)
p = d1 * x
p = substitute(p, [L], [L_])
pxx = -p * 1 + m * (diff(vx, x) + diff(vx, x))
pxy = -p * 0 + m * (diff(vx, y) + diff(vy, x))
pyy = -p * 1 + m * (diff(vy, y) + diff(vy, y))
p2ij = pxx ** 2 + 2 * pxy ** 2 + pyy ** 2
f = p2ij - 2 * p ** 2
f = substitute(f, [m, H0, L], [m_, H0_, L_])
print('1. Integrating...')
fx = integrate(f, (y, -H, H))
g = integrate(fx, (x, 0, L_))
g = substitute(g, [H0, L], [H0_, L_])
print('g=')
pprint(g)
print('='*50)
print(diff(g,a))
equations, variables = [], []
equations.append(diff(g, a))
equations.append(diff(g, d1))
equations.append(diff(g, a1))
variables.append(a)
variables.append(d1)
variables.append(a1)
print('=' * 100)
print('1. Solving all partial derivatives equal to 0')
result = solve(equations, variables)
print('1. Building plot')

