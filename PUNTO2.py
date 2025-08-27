A = [[2, 4, 6],
     [1, 3, 5]]

B = [[1, 2, 3],
     [4, 5, 6]]

suma    = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
resta   = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
division = [[A[i][j] / B[i][j] if B[i][j] != 0 else "∞" for j in range(len(A[0]))] for i in range(len(A))]

producto_punto = [[sum(A[i][k] * B[k][j] for k in range(len(B)))
                   for j in range(len(B[0]))] for i in range(len(A))]

producto_cruz = ([
    A[0][1]*B[0][2] - A[0][2]*B[0][1],
    A[0][2]*B[0][0] - A[0][0]*B[0][2],
    A[0][0]*B[0][1] - A[0][1]*B[0][0]
] if len(A)==1 and len(A[0])==3 and len(B)==1 and len(B[0])==3 else "Solo válido para vectores 1x3")

print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División:", division)
