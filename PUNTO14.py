import numpy as np
import matplotlib.pyplot as plt

V = float(input("Ingrese el voltaje de la fuente (V): "))
C_micro = float(input("Ingrese la capacitancia (μF): "))
R = float(input("Ingrese la resistencia (Ω): "))

C = C_micro * 1e-6

tau = R * C

t = np.linspace(0, 5*tau, 500)

Vc_carga = V * (1 - np.exp(-t / tau))   
Vc_descarga = V * np.exp(-t / tau)      

plt.figure(figsize=(8,5))
plt.plot(t, Vc_carga, label="Carga del capacitor", color="blue")
plt.plot(t, Vc_descarga, label="Descarga del capacitor", color="red")
plt.title(f"Circuito RC - Carga y Descarga\nτ = {tau:.4f} s")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje en el capacitor [V]")
plt.grid(True)
plt.legend()
plt.show()
