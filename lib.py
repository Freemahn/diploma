from sympy import *
import sympy
import random
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve


def substitute(func, vars, vals):
    f = func
    i = 0
    for v in vars:
        val = vals[i]
        f = f.subs(v, val)
        i = i + 1
    return f


def solve(equation, vars):
    print('-' * 50)
    s = list(nonlinsolve(equation, vars))
    print('Solving for variables', str(vars))
    solutions = list(s)
    print('Amount of solutions', len(solutions))
    result = []
    for args in solutions:
        print('New solution: ')
        tmp = []
        for i, arg in enumerate(args):
            print(vars[i],'=', end='')
            pprint(arg.evalf())
            tmp.append(arg)
        print('='*50)
        result.append(tmp)
    return result
