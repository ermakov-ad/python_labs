from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt

path_matrix = 'matrix_ep_2.txt'

with open(path_matrix) as f:
    lines = f.readlines()
    n = int(lines[0])
    a = []
    for i in range(n):
        a.append(list(map(float, lines[i+1].split())))
    b = np.array(list(map(float, lines[n+1].split())))
    A = np.array(a)
x = linalg.solve(A, b)
print(x)
fig, gr = plt.subplots()
gr.bar(np.linspace(0, len(x), len(x)), x)
gr.set_xlabel('index')
gr.set_ylabel('solution')
gr.grid(True)
plt.savefig('sistem with ' + str(n) + ' params.png')
