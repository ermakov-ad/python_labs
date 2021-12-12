from scipy import linalg
import numpy as np

path_matrix = 'test_matrix_ep_2.txt'

with open(path_matrix) as f:
    lines = f.readlines()
    n = int(lines[0])
    a = []
    for i in range(n):
        a.append(list(map(int, lines[i+1].split())))
    b = np.array(list(map(int, lines[n+1].split())))
    A = np.array(a)
x = linalg.solve(A, b)
print(x)
