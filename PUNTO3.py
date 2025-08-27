import math

x, y, z = 6, 8, 5   

r = math.sqrt(x**2 + y**2)
theta_cil = math.degrees(math.atan2(y, x))  
z_cil = z

rho = math.sqrt(x**2 + y**2 + z**2)
theta_esf = math.degrees(math.atan2(y, x))  
phi = math.degrees(math.acos(z / rho)) if rho != 0 else 0

print("Coordenadas rectangulares:")
print(f"x = {x}, y = {y}, z = {z}")

print("\nCoordenadas cilíndricas:")
print(f"r = {r:.2f}, θ = {theta_cil:.2f}°, z = {z_cil:.2f}")

print("\nCoordenadas esféricas:")
print(f"ρ = {rho:.2f}, θ = {theta_esf:.2f}°, φ = {phi:.2f}°")
