import math

P = 600000     
D = 0.05       
d = 0.02       


A_embolo = (math.pi * (D**2)) / 4           
A_anular = (math.pi * (D**2 - d**2)) / 4    

F_avance = P * A_embolo
F_retroceso = P * A_anular

print("Parámetros del cilindro neumático:")
print(f"Presión: {P/100000:.2f} bar")
print(f"Diámetro émbolo: {D*1000:.1f} mm")
print(f"Diámetro vástago: {d*1000:.1f} mm")

print("\nResultados:")
print(f"Área del émbolo: {A_embolo:.6f} m²")
print(f"Área anular: {A_anular:.6f} m²")
print(f"Fuerza de avance: {F_avance:.2f} N")
print(f"Fuerza de retroceso: {F_retroceso:.2f} N")
