import random

cantidad = int(input("¿Cuántos números aleatorios desea generar? "))
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

print("\nNúmeros aleatorios generados:")

for i in range(cantidad):
    numero = random.randint(minimo, maximo) 
    print(numero)
