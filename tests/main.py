from main.lib import *

init_printing()

a, b, c, d = symbols('a, b, c, d')
a1, b1, c1 = symbols('a1, b1, c1')
m, L, H, H0 = symbols('m, L, H, H0')
x, y = symbols('x, y')
v0, v1 = symbols('v0, v1')
d1, d2 = symbols('d1, d2')
H_, H0_, L_ = 1, 1, 10
d1_ = 1
m_ = 1
n = 2
kn = 12/5
vx = a * x * (x - L) * (y ** 2 - H ** 2) + \
     b * x * (x - L) * (y ** 2 - H ** 2) ** 2 + \
     v0 * (L - x) / L * (y ** 2 - H ** 2) ** n + \
     kn * v0 * (x / L) * (y ** 2 - H ** 2)
dxvx = diff(vx, x)
dyvy = -dxvx
print("dyvy=", dyvy)
print('='*50)
vy = integrate(dyvy, y)
vy = substitute(vy, [a, b, v0], [a1, b1, v1])

vx = substitute(vx, [L, H], [L_, H_])
vy = substitute(vy, [L, H], [L_, H_])
print("vx=", vx)
pprint(vx)
print('- '*100)
print("vy=", vy)
pprint(vy)
print('='*100)
p = d1 * x + (1 - d1 * L)/ L * x ** 2
p = substitute(p, [d1, L], [d1_, L_])
pxx = -p * 1 + m * (diff(vx, x) + diff(vx, x))
pxy = -p * 0 + m * (diff(vx, y) + diff(vy, x))
pyy = -p * 1 + m * (diff(vy, y) + diff(vy, y))
p2ij = pxx ** 2 + 2 * pxy ** 2 + pyy ** 2
f = p2ij - 2 * p ** 2
f = substitute(f, [d1, m, H, L], [d1_, m_, H_, L_])
print('1. Integrating...')
g = integrate(f, (x, 0, L_), (y, -H, H))
g = substitute(g, [H, L], [H_, L_])
# pprint(g)

equations, variables = [], []
equations.append(diff(g, a))
equations.append(diff(g, b))
equations.append(diff(g, v0))

equations.append(diff(g, a1))
equations.append(diff(g, b1))
equations.append(diff(g, v1))
variables.append(a)
variables.append(b)
variables.append(v0)
variables.append(a1)
variables.append(b1)
variables.append(v1)
print('=' * 100)
print('1. Solving all partial derivatives equal to 0')
result = solve(equations, variables)
print('1. Building plot')
vx1 = substitute(vx, variables, result)
print(vx1)
print('=' * 100)
vx1 = substitute(vx1, [d1, y, H, L], [d1_, 0, H_, L_])
print("vx1 = ", vx1)
print('=' * 100)
vy1 = substitute(vy, variables, result)
print(vy1)
print('-' * 100)
vy1 = substitute(vy1, [d1, H, L], [d1_, H_, L_])
print("vy1 = ", vy1)

# p1 = sympy.plotting.plot(vx1, xlim=(-(L_ + 1), (L_ + 1)), ylim=(-(50), (50)), ylabel='vx')








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
