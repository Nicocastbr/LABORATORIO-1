R0 = 100.0      
alpha = 0.00385 

A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12  

def rtd_resistance(T):
    """Resistencia de PT100 según IEC 60751."""
    if T >= 0:
        return R0 * (1 + A*T + B*T**2) 
    else:
        return R0 * (1 + A*T + B*T**2 + C*(T-100)*T**3) 

print("Temperatura [°C]   Resistencia [Ω]")
print("-" * 35)

for T in range(-200, 101): 
    R_T = rtd_resistance(T)
    print(f"{T:>6}            {R_T:>10.3f}")

T = 100
R_T_linear = R0 * (1 + alpha * T)
print("\nEjemplo con fórmula lineal:")
print(f"Temperatura: {T} °C")
print(f"Resistencia PT100 (lineal): {R_T_linear:.2f} Ω")
