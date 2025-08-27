v1 = [2, 4, 6]
v2 = [1, 3, 5]

print("Vector 1:", v1)
print("Vector 2:", v2)

suma = [v1[i] + v2[i] for i in range(3)]
resta = [v1[i] - v2[i] for i in range(3)]

producto_punto = sum(v1[i] * v2[i] for i in range(3))

producto_cruz = [
    v1[1]*v2[2] - v1[2]*v2[1],
    v1[2]*v2[0] - v1[0]*v2[2],
    v1[0]*v2[1] - v1[1]*v2[0]
]

division = [v1[i] / v2[i] if v2[i] != 0 else "∞" for i in range(3)]

print("\nResultados:")
print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División elemento a elemento:", division)
