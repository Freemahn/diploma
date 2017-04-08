def goin(func, vars, vals):
	f = func
	i = 0
	for v in vars:
		val = vals[i]
		f = f.subs(v, val)
		i = i + 1
	return f

def trap(func, variable, a, b, n):
	step = (b - a)/n
	t_prev = a
	t_cur = a + step
	equation = 0.
	while t_cur < b:
		s = step*(func.subs(variable, t_cur) + func.subs(variable, t_prev))/2
		equation = equation + s
		t_prev = t_cur
		t_cur += step
	return equation

def boost_trap(func, variable, a, b, step):
	b -= step
	t_cur = a + step
	fi = []
	fi.append(func.evalf(subs={variable: a})/2)
	while t_cur < b:
		fi.append(func.evalf(subs={variable: t_cur}))
		t_cur += step
	fi.append(func.evalf(subs={variable: t_cur})/2)
	return sum(fi)*step