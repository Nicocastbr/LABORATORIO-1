def robot_cartesiano():
    return "Robot Cartesiano: posee 3 articulaciones prismáticas (lineales)."

def robot_cilindrico():
    return "Robot Cilíndrico: posee 1 articulación rotacional y 2 prismáticas."

def robot_esferico():
    return "Robot Esférico: posee 2 articulaciones rotacionales y 1 prismática."

print("Tipos de Robots")
print("1. Cartesiano")
print("2. Cilíndrico")
print("3. Esférico")

opcion = int(input("Seleccione una opción (1-3): "))

if opcion == 1:
    print(robot_cartesiano())
elif opcion == 2:
    print(robot_cilindrico())
elif opcion == 3:
    print(robot_esferico())
else:
    print("Opción inválida.")
