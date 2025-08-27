R0 = 100      
alpha = 0.00385  

T = 100  

R_T = R0 * (1 + alpha * T)

print(f"Temperatura: {T} °C")
print(f"Resistencia del PT100: {R_T:.2f} Ω")
