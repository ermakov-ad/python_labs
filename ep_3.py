import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

file_path = 'func_ep3.txt'
start_data = np.loadtxt(file_path)
data = np.copy(start_data)
l = len(start_data)
A = np.diag(-1*np.ones(l+1))
A = np.delete(A, 0, axis=1)
A = np.delete(A, l, axis=0)
A += np.diag(np.ones(l))
#data = np.zeros((256,l))
#data[0] = np.copy(start_data)
#for i in range(1, 256):
#    data[i] = data[i-1] -0.5 * A.dot(data[i-1])
#    data[i][0] = data[i][l-1]
T = np.linspace(0, l-1, l)

fig, ax = plt.subplots()

ax.set_xlim(0, 50)
ax.set_ylim(0, 10)
ax.grid(True)

line, = ax.plot(T, start_data)

def func(i):
    global data
    data = data - 0.5 * A.dot(data)
    data[0] = data[len(data) - 1]
    line.set_ydata(data)

    return line,

ani = FuncAnimation(fig, func, interval=10, blit=False, frames=256, repeat=False)
#plt.show()
ani.save("signal.gif", writer='pillow', fps=60)