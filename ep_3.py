import matplotlib.pyplot as plt
from scipy.integrate import odeint as oi
import sympy.plotting.plot as symplot
import sympy
import numpy as np
import math

y0 = math.sqrt(2)
f = sympy.symbols('f', cls=sympy.Function)
x = sympy.Symbol('x')
g: object = sympy.dsolve(f(x).diff(x) + 2*f(x), f(x), ics={f(0):y0}, hint='separable').rhs
print(g)

def dydx(y, x):
    return -2*y

X = np.linspace(0, 10, 1000)
Ysci = oi(dydx, y0, X)
Ysym = []
delta = []
for i in range(len(X)):
    Ysym.append(g.evalf(subs={x:X[i]}))
    delta.append(Ysci[i] - Ysym[i])
fig, gr = plt.subplots()
plt.grid(True)
gr.plot(X, Ysci)
gr.set_title('scipy solution')
gr.set_xlabel('x')
gr.set_ylabel('y(x)')
plt.savefig('ep_3 solutions\\scipy solution.png')
gr.clear()
plt.grid(True)
gr.plot(X, Ysym)
gr.set_title('sympy solution')
gr.set_xlabel('x')
gr.set_ylabel('y(x)')
plt.savefig('ep_3 solutions\\sympy solution.png')
gr.clear()
plt.grid(True)
gr.plot(X, delta)
gr.set_title('scipy solution - sympy solution')
gr.set_xlabel('x')
gr.set_ylabel('y(x)')
plt.savefig('ep_3 solutions\\scipy solution - sympy solution.png')

p = symplot(g, xlim=(0, 10), ylim=(0, 2))
p.show()
