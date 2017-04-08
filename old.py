from sympy import *
import random


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


c0, c1, c2, c3, c4, c5, t, x, y = symbols('c0, c1, c2, c3, c4, c5, t, x, y')
f = c2 * x ** 2 + c4 * x ** 4  # c0 + c1*x + c2*x**2 + c3*x**3 + c4*x**4 + c5*x**5
f_ = diff(f, x)
g = sqrt(1 + f_ ** 2) + f

# test = sin(x) - cos(x**2) + 3*sqrt(10)*sqrt(x**2 + 1)
# print(' testval = ', trap(test, -5, 5, 100).evalf())

# random.seed(20)

vector = []
vec = []
mas = []
approx_0 = []
approx_1 = []

# vector.append(c0)

# vector.append(c1)
vector.append(c2)
# vector.append(c3)
vector.append(c4)
# vector.append(c5)

for var in vector:
    d = diff(g, var)
    if d.is_constant():
        continue
    mas.append(d);

jacob = []
step = 0
print(" vector = ", vector)

for fo in mas:
    for v in vector:
        jacob.append(diff(fo, v))

# approx_0.append(0)
approx_0.append(-1 / 10)
# approx_0.append(0)
approx_0.append(1 / 750)
# approx_0.append(0)
while (step < 15):
    step = step + 1
    print("________________________")
    print("step = ", step)
    v = []
    i = 0
    for fo in mas:
        foo = goin(fo, vector, approx_0)
        # v.append(foo.evalf())
        v.append(trap(foo, -5, 5, 100).evalf())
    F_Zk = Matrix(2, 1, v)
    j = []
    for fo in jacob:
        foo = goin(fo, vector, approx_0)
        # j.append(foo.evalf())
        j.append(trap(foo, -5, 5, 100).evalf())
    F_ = Matrix(2, 2, j)
    F_inv = F_.inv()
    Zk = Matrix(2, 1, approx_0)
    res = Zk - F_inv * F_Zk
    approx_0 = []
    for r in res:
        approx_0.append(r)
    print(approx_0, "\n == ")
    print(F_Zk)


