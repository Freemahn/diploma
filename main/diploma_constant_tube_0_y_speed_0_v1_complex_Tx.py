from main.lib import *

init_printing()

b, c = symbols('b, c')
args_a = symbols('a0, a1, a2, a3,a4,a5,a6,a7,a8, a9, a10')
args_d = symbols('d0, d1')
m, L, H0 = symbols('m, L, H0')
x,  y = symbols('x, y')
v0, v1 = symbols('v0, v1')



H0_, L_ = 2, 15
m_, v0_ = 1, 4
H = H0
n = 2 # number of args
a = args_a[:n]
d = args_d
Tx = a[0] + a[1] * x


vx = v0 * (1 - x / L) + (1 - x ** 2 / L ** 2) * (H ** 2 - y ** 2) * Tx
p = d[0] + d[1] * x

print("vx=", vx)
print("p=", p)


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
vy = 0


def plot_vx_by_x():
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
        print("vx1 = ", vx2)
        print('=' * 100)
        pl1 = sympy.plotting.plot(vx2, xlim=(-L_, (L_ + 0.1)), ylim=(-(10 + 1), (10 + 1)), ylabel='vx')

        vx3 = substitute(vx1, [x], [0])
        print("vx1 = ", vx3)
        print('=' * 100)
        pl2 = sympy.plotting.plot(vx3, xlim=(-L_, (L_ + 0.1)), ylim=(-(10 + 1), (10 + 1)), ylabel='vx')


def plot_vx_by_y():
    if len(result) == 0:
        print('No solutions!')
    else:
        print('2. Building plot')
        vy1 = substitute(vy, variables, result[0])
        print('=' * 100)
        vy1 = substitute(vy1, [v0, H0, L], [v0_, H0_, L_])
        print("vy = ", vy)
        print("vy1 = ", vy1)
        print('-' * 100)
        vy1 = substitute(vy1, [x], [0])
        print("vy1 = ", vy1)
        print(nonlinsolve([vy1], [y]))
        print(substitute(vy1, [y], [0]))
        p2 = sympy.plotting.plot(vy1, xlim=(-1, (1 + 0.1)), ylim=(-(0.3), (0.3)), ylabel='vy')

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


derivatives_d = []
for i in range(0, 2):
    derivatives_d.append(diff(g, d[i]))
    print('diff(g, d[{0}])={1}'.format(i,  derivatives_d[i]))



p2 = substitute(p, [x], [ L_]) - 2
p1 = substitute(p, [x], [-L_]) + 1
print("p1=", p1)
print("p2=", p2)
print('=' * 100)

# In[8]:


print('1. Solving all partial derivatives equal to 0')
variables = list(a)+list(d)
result = solve(derivatives_a + derivatives_d, variables)
plot_vx_by_x()
# plot_vx_by_y()








