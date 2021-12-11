import sympy

#p, y, x = sympy.symbols('p λ μ')
path_matrix = 'matrix_ep_1.txt'

with open(path_matrix) as f:
    lines = f.readlines()
    A = []
    for i in range(len(lines)):
        A.append(list(map(str, lines[i].split())))
B = sympy.Matrix(A)
ans = list(B.eigenvals().keys())
print(ans)
