from sympy import *
import sympy
import random
from sympy.core.symbol import symbols
# from sympy.solvers.solveset import nonlinsolve
print(sympy.__version__)

def goin(func, vars, vals):
    f = func
    i = 0
    for v in vars:
        val = vals[i]
        f = f.subs(v, val)
        i = i + 1
    return f


def trap(func, a, b, n):
    step = (b - a) / n
    t_prev = a
    t_cur = a + step
    equation = 0
    while t_cur < b:
        s = step * (func.subs(x, t_cur) + func.subs(x, t_prev)) / 2
        equation = equation + s
        t_prev = t_cur
        t_cur += step
    return simplify(equation)


a, b, c, m, L, H, x, y = symbols('a, b, c, m, L, H, x, y')
v = (a + b * x) * (1 - (y ** 2) / (H ** 2))
p = c * x
pxx = -p + 2 * m * diff(v, x)
pxy = m * diff(v, y)
pyy = -p
p2ij = pxx ** 2 + 2*pxy**2+ pyy ** 2
f = p2ij - 2*p**2
print(f)

f1 =  a + b*x + c*y
r = goin(f1, [x], [10])
# print(r)
integr = integrate(f,(x, 0, L), (y,-H,H))
diff_a = diff(integr, a)
diff_b = diff(integr, b)
diff_c = diff(integr, c)
print(integr)
print('*'*50)
print(diff_a)
print(diff_b)
print(diff_c)

x, y, z = symbols('x, y, z', real=True)
# nonlinsolve([x*y - 1, 4*x**2 + y**2 - 5], [x, y])