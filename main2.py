from sympy import *
import sympy
import random
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve
from lib import *
init_printing()
a0, b, c, d,d1,d2, d3 = symbols('a0, b, c, d, d1, d2, d3')
a1,a2,a3,  b1, c1 = symbols('a1,a2,a3, b1, c1')
m, L, H0 = symbols('m, L, H0')
x, y = symbols('x, y')
v0, v1 = symbols('v0, v1')

H0_, L_ = 1, 10
m_, v0_ = 1, 1
H = H0_ - 0.0 *  (2* x / L_  - 1) ** 2
vx = (v0_ + (a0)* x * (L_ - x)) * (H ** 2 - y ** 2)
dxvx = diff(vx, x)
dyvy = - dxvx
print("dyvy=", dyvy)
print('='*50)
vy = integrate(dyvy, y)
# vy = substitute(vy, [a, v0], [a1, v1])
# vx = substitute(vx, [L, H0], [L_, H0_])
# vy = substitute(vy, [L, H0], [L_, H0_])
print("vx=", vx)
# pprint(vx)
print('- '*100)
print("vy=", vy)
# pprint(vy)
print('='*100)
p = d1 * x + (1 - d1 * L_)/ L_ * x ** 2
pxx = -p * 1 + m * (diff(vx, x) + diff(vx, x))
pxy = -p * 0 + m * (diff(vx, y) + diff(vy, x))
pyy = -p * 1 + m * (diff(vy, y) + diff(vy, y))
p2ij = pxx ** 2 + 2 * pxy ** 2 + pyy ** 2
f = p2ij - 2 * p ** 2 #f = substitute(f, [m, H0, L], [m_, H0_, L_])
print("f=", f)
print('1. Integrating ...')
fx = integrate(f, (y, -H, H)) #fx = substitute(fx, [m, H0, L], [m_, H0_, L_])
print('2. Integrating ...')
g = integrate(fx, (x, 0, L_))
g = substitute(g, [H0, L], [H0_, L_])
print('g=')
pprint(g)
print('='*50)

d_a0 = diff(g, a0)
d_a1 = diff(g, a1)
d_a2 = diff(g, a2)
d_a3 = diff(g, a3)
d_d1 = diff(g, d1)
# d_d2 = diff(g, d2)
p2 = substitute(p,[x], [L_]) - 1
p1 = substitute(p, [x], [0])
print("d_a0=", d_a0)
# print("d_a1=", d_a1)
# print("d_a2", d_a2)
# print("d_a3", d_a3)

print("d_d1=", d_d1)
# print("d_d2=", d_d2)
print("p2=", p2)
print('=' * 100)
print('1. Solving all partial derivatives equal to 0')
result = solve([d_a0, d_d1, p2], [a0, d1])
if len(result) == 0:
    print('No solutions!')
else:
    print('1. Building plot')
    vx1 = substitute(vx, [a0, d1], result[0])
    print('=' * 100)
    vx1 = substitute(vx1, [v0, y, H0, L], [1, 0, H0_, L_])
    print("vx = ", vx)
    # vx1 = substitute(vx1, [y,H0, L], [0, H0_,L_])
    print("vx1 = ", vx1)
    print('=' * 100)
    print(substitute(vx1, [x], [0]))
    p1 = sympy.plotting.plot(vx1, xlim=(0, (L_)), ylim=(-(5), (5)), ylabel='vx')
