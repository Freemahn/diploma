from sympy import *
import sympy
import random
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve
from lib import *

init_printing()

a, b, c, d,d1,d2 = symbols('a, b, c, d, d1, d2')
a1, b1, c1 = symbols('a1, b1, c1')
m, L, H, H0 = symbols('m, L, H, H0')
x, y = symbols('x, y')
v0, v1 = symbols('v0, v1')
# d1, d2 = symbols('d1, d2')
H_, H0_, L_ = 1, 1, 10
# d2_ = 1
m_ = 1
n = 2
# kn = 12/5
vx = (v0 + a*x*(x - L)) * (y ** 2 - H ** 2)
dxvx = diff(vx, x)
dyvy = -dxvx
print("dyvy=", dyvy)
print('='*50)
vy = integrate(dyvy, y)
vy = substitute(vy, [a, v0], [a1, v1])

# vx = substitute(vx, [L, H], [L_, H_])
# vy = substitute(vy, [L, H], [L_, H_])
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
f = substitute(f, [m, H, L], [m_, H_, L_])
print('1. Integrating...')
g = integrate(f, (x, 0, L_), (y, -H_, H_))
g = substitute(g, [H, L], [H_, L_])
# pprint(g)

equations, variables = [], []
equations.append(diff(g, a))
equations.append(diff(g, d1))
equations.append(diff(g, a1))
equations.append(p-1)
# equations.append(diff(g, v0))

variables.append(a)
variables.append(d1)
variables.append(d2)
variables.append(a1)
# variables.append(v0)
print('=' * 100)
print('1. Solving all partial derivatives equal to 0')
result = solve(equations, variables)
print('1. Building plot')
vx1 = substitute(vx, variables, result[0])
print(vx1)
print('=' * 100)
vx1 = substitute(vx1, [v0, y, H, L], [1, 0, H_, L_])
print("vx1 = ", vx1)
print('=' * 100)
vy1 = substitute(vy, variables, result)
print(vy1)
print('-' * 100)
vy1 = substitute(vy1, [v0, x, H, L], [1, 0,  H_, L_])
print("vy1 = ", vy1)

p1 = sympy.plotting.plot(vx1, xlim=(-(L_ + 1), (L_ + 1)), ylim=(-(H_ + 1), (H_ + 1)), ylabel='vx')
p2 = sympy.plotting.plot(vy1, xlim=(-(L_ + 1), (L_ + 1)), ylim=(-(H_ + 1), (H_ + 1)), ylabel='vy')








#
# print('Part 2')
# print("vx=", vx)
# print()
# print("g=", g)
# print()
# dxvx = diff(vx, x)
# dyvy = -dxvx
# print("dyvy=", dyvy)
# print()
# vy = integrate(dyvy, (y, -H, H))
# vy = substitute(vy, [H, L], [H_, L_])
# print(vy)
# equations = []
# variables = []
# equations.append(diff(vy, a))
# equations.append(diff(vy, b))
# equations.append(diff(vy, v0))
# variables.append(a)
# variables.append(b)
# variables.append(v0)
# print('2. Solving all partial derivatives equal to 0')
# print(diff(vy, a))
# print(diff(vy, b))
# print(diff(vy, v0))
# result = solve(equations, variables)
# print(result)
# print('2. Building plot')
# vx2 = substitute(vy, variables, result)
# print('2. ================================')
# vx2 = substitute(vx2, [y, H, L], [0, H_, L_])
# vx2 = substitute(vx2, [d1, d2], [d1_, d2_])
# print(vx2)
#
# # p2 = sympy.plotting.plot(vx2, xlim=(-(L_ + 1), (L_ + 1)), ylim=(-(50), (50)), ylabel='vy')
