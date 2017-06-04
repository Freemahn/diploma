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
f = c0 + c1 * x + c2 * x ** 2 + c3 * x ** 3 + c4 * x ** 4 + c5 * x ** 5
f_ = diff(f, x)
g = sqrt(1 + f_ ** 2) + f

test = sin(x) - cos(x ** 2) + 3 * sqrt(10) * sqrt(x ** 2 + 1)
print(' testval = ', trap(test, -5, 5, 100).evalf())

# random.seed(20)

vector = []
vec = []
mas = []
approx_0 = []
approx_1 = []

vector.append(x)
vector.append(y)

jacob = []
step = -1
print(" vector = ", vector)

mas.append(sin(x + y) - 1.6 * x)  # x*y - 1) #sin(x+y) - 1.6*x)
mas.append(x ** 2 + y ** 2 - 1)  # x - y) #x**2 + y**2 - 1)
for f in mas:
    for v in vector:
        jacob.append(diff(f, v))
approx_0.append(0)  # 0
approx_0.append(-1)  # -5) # -1

while (step < 6):
    step = step + 1
    print("________________________")
    print("step = ", step)
    v = []
    i = 0
    for f in mas:
        foo = goin(f, vector, approx_0)
        v.append(foo.evalf())
    # v.append(trap(foo,-5, 5, 100).evalf())
    F_Zk = Matrix(2, 1, v)
    print(" F_Zk = ", v)
    j = []
    for f in jacob:
        foo = goin(f, vector, approx_0)
        j.append(foo.evalf())
    # j.append(trap(foo,-5, 5, 100).evalf())
    F_ = Matrix(2, 2, j)
    print(" F_ = ", F_)
    F_inv = F_.inv()
    Zk = Matrix(2, 1, approx_0)
    res = Zk - F_inv * F_Zk
    approx_0 = []
    for r in res:
        approx_0.append(r.round(3))

        # foo = goin(mas[3], vector, approx_0)
        # print(approx_0)
        # print("f = ", trap(foo,-5, 5, 100).evalf())
print("appr = ", approx_0)
foo = goin(mas[0], vector, approx_0)
print("f1 = ", trap(foo, -5, 5, 100).evalf())
foo = goin(mas[1], vector, approx_0)
print("f2 = ", trap(foo, -5, 5, 100).evalf())
# M = Matrix(( [1, 2, 3], [3, 6, 2], [2, 0, 1] ))
# mat = Matrix(([-1.06, 0.54], [0, -2]))
# print(mat.inv())

# print("started", sin(pi/4 + 5).evalf())
# print(trap(sin(x) - cos(x),-5, 5, 100).evalf())
# print("1 = ", diff(g, c1))
# print("2 = ", diff(g, c2))
# print("3 = ", diff(g, c3))
# g1 = diff(g, c1)
# g2 = diff(g, c2)
# g3 = diff(g, c3)

