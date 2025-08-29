import numpy as np
import matplotlib.pyplot as plt
import control as ctrl  

wn = float(input("Ingrese la frecuencia natural ωn: "))
zeta = float(input("Ingrese el coeficiente de amortiguamiento ζ: "))
K = float(input("Ingrese la ganancia K: "))

num = [K * wn**2]
den = [1, 2*zeta*wn, wn**2]
G = ctrl.TransferFunction(num, den)

if zeta == 1:
    tipo = "Críticamente amortiguado"
elif zeta < 1 and zeta > 0:
    tipo = "Subamortiguado"
elif zeta > 1:
    tipo = "Sobreamortiguado"
elif zeta == 0:
    tipo = "No amortiguado (oscilatorio)"
else:
    tipo = "Inestable (ζ < 0)"

print(f"\nEl sistema es: {tipo}\n")
print(f"Función de transferencia: {G}\n")

t, y = ctrl.step_response(G)

plt.figure(figsize=(8,5))
plt.plot(t, y, label=f"Respuesta (ζ={zeta}, K={K})", color="blue")
plt.axhline(K, color="red", linestyle="--", label="Valor final esperado")
plt.title(f"Respuesta al Escalón - Sistema {tipo}")
plt.xlabel("Tiempo [s]")
plt.ylabel("Salida")
plt.grid(True)
plt.legend()
plt.show()
