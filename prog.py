from my_integration import *
from sympy import *
import random

# ========== variables and functions definition ========== #
c0, c1, c2, c3, c4, c5, t, x, y = symbols('c0, c1, c2, c3, c4, c5, t, x, y')

func5 = c0 + c1 * x + c2 * x ** 2 + c3 * x ** 3 + c4 * x ** 4 + c5 * x ** 5
func2_4 = c2 * x ** 2 + c4 * x ** 4
test = sin(x) - cos(x ** 2) + 3 * sqrt(10) * sqrt(x ** 2 + 1)

f = func5
f_ = diff(f, x)
g = sqrt(1 + f_ ** 2) + f

eps = 0.001
a = -5
b = 5
segments = 100
step = (b - a) / segments

# numEquations = 5
# constants = symbols('a1:%d'%numEquations)
# eq = 1
# for c in constants:
#	eq = eq + c
# print(eq.subs(constants[1], 777))

variables = {}
vec = []
mas = []
approx_0 = []

# seq = symbols('c1:%d'%3) #(c1, c2, c3, c4, c5)
# seq = (c2, c4)
# variables = variables.fromkeys(seq, 1.)

variables[c0] = 1
variables[c1] = 2
variables[c2] = 3
variables[c3] = 4
variables[c4] = 5
variables[c5] = 6
# vector.append(c0)
# vector.append(c1)
# vector.append(c2)
# vector.append(c3)
# vector.append(c4)
# vector.append(c5)
consts = []
for var in variables.keys():
    d = diff(g, var)
    if d.is_constant():
        consts.append(var)
        continue
    mas.append(d)
for c in consts:
    del variables[c]

print(variables)
dimension = len(list(variables.keys()))
jacob = []
# approx_0.append(0)
# approx_0.append(0)
# approx_0.append(0)
# approx_0.append(1/10)
# approx_0.append(1/750)
# print(approx_0)
# print(vector)
# print(" vector = ", vector)
for foo in mas:
    for v in variables.keys():
        jacob.append(diff(foo, v))
s = 0

while (s < 15):
    s = s + 1
    # print("f = ", trap(f.subs(variables),x,-5, 5, 100))
    p = 0
    print("____________________________________________")
    print("step = ", s)
    v = []
    for foo in mas:
        v.append(trap(foo.subs(variables), x, -5, 5, 100))
    F_Zk = Matrix(dimension, 1, v)
    j = []
    for foo in jacob:
        j.append(trap(foo.subs(variables), x, -5, 5, 100))  # trap(foo,-100, 100, 1000).evalf())

    F_ = Matrix(dimension, dimension, j)
    F_inv = F_.inv()

    Zk = Matrix(dimension, 1, list(variables.values()))
    res = Zk - F_inv * F_Zk

    i = -1
    for key in variables.keys():
        i = i + 1
        variables[key] = res[i].round(3)
    # accuracy = trap(mas[0].subs(variables),x,-5, 5, 100)
    print(variables)

print(" ======= FINISHED =======\n\n")
print(" =======  RESULT  =======")
p = 0
v = list(variables.keys())
for foo in mas:
    print(v[p], " equation: ", trap(foo.subs(variables), x, -5, 5, 100))
    p = p + 1

print("\n \n answer = ", variables)

# M = Matrix(( [1, 2, 3], [3, 6, 2], [2, 0, 1] ))
# mat = Matrix(([-1.06, 0.54], [0, -2]))
# print(mat.inv())
