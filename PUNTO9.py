import math

def volumen_prisma():
    largo = float(input("Ingrese el largo de la base: "))
    ancho = float(input("Ingrese el ancho de la base: "))
    altura = float(input("Ingrese la altura del prisma: "))
    return largo * ancho * altura

def volumen_piramide():
    base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura de la pirámide: "))
    return (base * altura) / 3

def volumen_cilindro():
    radio = float(input("Ingrese el radio de la base: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    return math.pi * (radio ** 2) * altura

def volumen_cono_truncado():
    R = float(input("Ingrese el radio mayor: "))
    r = float(input("Ingrese el radio menor: "))
    h = float(input("Ingrese la altura: "))
    return (1/3) * math.pi * h * (R**2 + R*r + r**2)

print("Cálculo de Volúmenes")
print("1. Prisma rectangular")
print("2. Pirámide")
print("3. Cilindro")
print("4. Cono truncado")

opcion = int(input("Seleccione una opción (1-4): "))

if opcion == 1:
    volumen = volumen_prisma()
elif opcion == 2:
    volumen = volumen_piramide()
elif opcion == 3:
    volumen = volumen_cilindro()
elif opcion == 4:
    volumen = volumen_cono_truncado()
else:
    print("Opción inválida.")
    volumen = None

if volumen is not None:
    print(f"\nEl volumen calculado es: {volumen:.2f} unidades cúbicas")
