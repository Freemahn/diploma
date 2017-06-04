from main.lib import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
init_printing()

args_a = symbols('a0, a1, a2, a3,a4,a5,a6,a7,a8, a9, a10')
args_b = symbols('b0, b1, b2, b3,b4,b5,b6,b7,b8, b9, b10')
args_d = symbols('d0, d1,d2, d3,d4,d5')
m, L, H0 = symbols('m, L, H0')
x,  y = symbols('x, y')
v0, v1 = symbols('v0, v1')



H0_, L_ = 1, 15
m_, v0_ = 2, 3
H = H0
n = 5 # number of args a vx
k = 2 # number of args p
l = 4 #  vy
a = args_a[:n]
b = args_b[:l]
d = args_d[:k]
Tx = a[0] + a[1] * x  + a[2] * x ** 2 + a[3] * y ** 2 #+ a[4] * x ** 3
Qx = b[0] * y + b[1] * x * y  + b[2] * x * y **2 + b[3] * y ** 3

vx =   (1 / 2) * v0 * (1 - x / L) * (1 - y ** 4 / H ** 4) \
     + (3 / 5) * v0 * (1 + x / L) * (1 - y ** 2 / H ** 2) \
     + (1 - x ** 2 / L ** 2) * (1 - y ** 2 / H ** 2) * Tx
print("vx=", vx)

vy =  (1 - x ** 2 / L ** 2) * (1 - y ** 2 / H ** 2) * Qx
print("vy=", vy)
p = d[0] + d[1] * x #+ d[2] + x ** 2 #+ d[3] * y ** 2
print("p=", p)
p2 = substitute(p, [x], [ L_]) - 3
p1 = substitute(p, [x], [-L_]) - 2
print("p1=", p1)
print("p2=", p2)
print('=' * 100)


dxvx = diff(vx, x)
dyvy = diff(vy, y)
dxedy =  dxvx + dyvy #dxvx - dyvy
print("dyvy=", dyvy)
# vy = integrate(dyvy, y)
# print("vy=", vy)
# # print('='*50)
# vy = 0

def check_profiles():
    # checking profiles
    print("vx(-L, y) =", substitute(vx, [x], [-L]))
    print("vx(L, y) =", substitute(vx, [x], [L]))
    print("vx(0, y) =", substitute(vx, [x], [0]))
    print("vx(L, y) =", substitute(vx, [x], [L]))
    print("H(0) =", substitute(H, [x], [0]))
    print("H(L) =", substitute(H, [x], [L]))
    print("H(-L) =", substitute(H, [x], [-L]))
    print("H(L) =", substitute(H, [x], [L]))

check_profiles()


def plot_vx():
    global result
    if len(result) == 0:
        print('No solutions for vx(x,0)!')
    else:
        print('1. Building plot')
        vx1 = substitute(vx, variables, result[0])
        print('=' * 100)
        vx1 = substitute(vx1, [v0, H0, L], [v0_, H0_, L_])
        print("vx = ", vx)
        print("vx1 = ", vx1)
        print('-' * 100)


        vx2 = substitute(vx1, [y], [0])
        print("vx(x,0) = {}".format(vx2))
        print('=' * 100)
        pl1 = plot(vx2, xlim=(-L_-0.1, (L_ + 0.1)), ylim=(-(5 - 0.1), (5 + 0.1)), ylabel='vx(x,0)')


        vx3 = substitute(vx1, [x], [0])
        print("vx(0,y) = {}".format(vx3))
        print("vx(-H0,y) = {}".format(substitute(vx1, [x], [-H0_ ])))
        print("vx(H0,y) = {}".format(substitute(vx1, [x], [H0_ ])))


        print('=' * 100)
        p1 = plot(
            vx3,
            xlim=(-H0_ - 0.1, H0_ + 0.1), ylim=(-0 - 0.1, (10 + 0.1)), ylabel='vx(dx,y)', show=false, line_color='black')
        p21 = plot(substitute(vx1, [x], [-L_ + 1 ]),show=false, line_color='brown')
        p22 = plot(substitute(vx1, [x], [-L_/2]), show=false, line_color='blue')
        p23 = plot(substitute(vx1, [x], [L_ / 2 ]),show=false, line_color='green')
        p24 = plot(substitute(vx1, [x], [L_-1]), show=false, line_color='yellow')
        p1.extend(p21)
        p1.extend(p22)
        p1.extend(p23)
        p1.extend(p24)
        p1.show()




def plot_vy():
    global result
    if len(result) == 0:
        print('No solutions for vy!')
    else:
        print('2. Building plot')
        print(vy)
        vy1 = substitute(vy, variables, result[0])
        print('=' * 100)
        vy1 = substitute(vy1, [v0, H0, L], [v0_, H0_, L_])
        print("vy = ", vy)
        print("vy1 = ", vy1)
        print('-' * 100)
        vy2 = substitute(vy1, [x], [0])
        print("vx(x,0) = {}".format(vy2))
        print('=' * 100)
        # pl1 = plot(vy2, xlim=(-L_-0.1, (L_ + 0.1)), ylim=(-(5 - 0.1), (5 + 0.1)), ylabel='vx(x,0)')

        vy3 = substitute(vy1, [x], [0])
        print("vy(0,y) = {}".format(vy3))
        print("vy(0,y) = {}".format(substitute(vy1, [x], [-H0_])))
        print("vy(0,y) = {}".format(substitute(vy1, [x], [H0_])))

        print('=' * 100)
        p2 = plot(
            vy3,
            xlim=(-H0_*10 - 0.1, H0_*10 + 0.1), ylim=(-L_ - 0.1, (L_ + 0.1)), ylabel='vy(dx,y)', show=false,
            line_color='black')
        p21 = plot(substitute(vy1, [x], [-L_ + 2]), show=false, line_color='brown')
        p22 = plot(substitute(vy1, [x], [-L_ / 2]), show=false, line_color='blue')
        p23 = plot(substitute(vy1, [x], [L_ / 2]), show=false, line_color='green')
        p24 = plot(substitute(vy1, [x], [L_ - 2]), show=false, line_color='yellow')
        p2.extend(p21)
        p2.extend(p22)
        p2.extend(p23)
        p2.extend(p24)
        p2.show()

pxx = -p * 1 + m * (diff(vx, x) + diff(vx, x))
pxy = -p * 0 + m * (diff(vx, y) + diff(vy, x))
pyy = -p * 1 + m * (diff(vy, y) + diff(vy, y))
p2ij = pxx ** 2 + 2 * pxy ** 2 + pyy ** 2
f = p2ij - 2 * (p ** 2)
# f = substitute(f, [v0,v1, m, H0, L], [v0_,v1_, m_, H0_, L_])
print("f=", f)
print('1. Integrating ...')
fx = integrate(f, (y, -H, H))
# fx = substitute(fx, [v0,v1, m, H0, L], [v0_,v1_, m_, H0_, L_])
print("fx=", fx)
print('2. Integrating ...')
g = integrate(fx, (x, -L_, L_))
# g = substitute(g, [v0,v1, m, H0, L], [v0_,v1_, m_, H0_, L_])
print('g=', end='')
pprint(g)
print('=' * 50)

g = substitute(g, [v0, m, H0, L], [v0_, m_, H0_, L_])
print("g={}".format(g))
derivatives_a = []
for i in range(0, n):
    derivatives_a.append(diff(g, a[i]))
    print('diff(g, a[{0}])={1}'.format(i,  derivatives_a[i]))

derivatives_b = []
for i in range(0, l):
    derivatives_b.append(diff(g, b[i]))
    print('diff(g, b[{0}])={1}'.format(i,  derivatives_b[i]))

derivatives_d = []
for i in range(0, k):
    derivatives_d.append(diff(g, d[i]))
    print('diff(g, d[{0}])={1}'.format(i,  derivatives_d[i]))







print('1. Solving all partial derivatives equal to 0')
variables = list(a)+list(b) + list(d)
result = solve(derivatives_a + derivatives_b + derivatives_d + [dxedy], variables)
plot_vx()
plot_vy()








