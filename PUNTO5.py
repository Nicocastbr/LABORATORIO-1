import math

def rotacion_x(angulo):
    theta = math.radians(angulo)  
    return [
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta),  math.cos(theta)]
    ]

def rotacion_y(angulo):
    theta = math.radians(angulo)
    return [
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ]

def rotacion_z(angulo):
    theta = math.radians(angulo)
    return [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
        [0, 0, 1]
    ]

angulo = 45  

print(f"Ángulo usado: {angulo}°\n")

print("Matriz de rotación en X:")
for fila in rotacion_x(angulo):
    print(fila)

print("\nMatriz de rotación en Y:")
for fila in rotacion_y(angulo):
    print(fila)

print("\nMatriz de rotación en Z:")
for fila in rotacion_z(angulo):
    print(fila)
