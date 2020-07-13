import sympy as sp
import numpy as np
# x=sp.Symbol('x')
# y=sp.Symbol('y')
# f=4*x**2+2*y
# f_diff=f.diff(x)
# ef=sp.lambdify((x,y),f)
# print(ef(1,5))


from sympy.parsing.sympy_parser import parse_expr as parse
# eq_strings=["-3*x-4*y-2*z=1","5*x-2*y+1*z=1","2*x+4*y+4*z=1"]
# symbols=[sp.Symbol(i)for i in "xyz"]
# eq_tuples=[(i.split('=')) for i in eq_strings]
# eq=[(np.array(sp.linear_eq_to_matrix(parse(i[0]),symbols)[0]),parse(i[1]))for i in eq_tuples]
# coMatrix=np.vstack(tuple(i[0]for i in eq))
# AugMatrix=np.vstack(tuple(np.append(i[0],i[1])for i in eq))
# print(AugMatrix)

eq_string='exp(x)+4*x+2'
x=sp.Symbol('x')
eq=parse(eq_string)
eq_diff=eq.diff(x)
ef_diff=sp.lambdify(x,eq.diff(x))
print(ef_diff(2))