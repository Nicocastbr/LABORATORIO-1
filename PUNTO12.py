import numpy as np
import matplotlib.pyplot as plt

def resistencia_pt100(T):
    """Calcula la resistencia de un sensor PT100 en función de la temperatura."""
    R0 = 100  
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12

    if T >= 0:
        return R0 * (1 + A * T + B * T**2)
    else:
        return R0 * (1 + A * T + B * T**2 + C * (T - 100) * T**3)

temperaturas = np.arange(-200, 201, 1)

resistencias = [resistencia_pt100(T) for T in temperaturas]

plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, label='Curva de Resistencia PT100')
plt.title('Comportamiento de un Sensor PT100: Resistencia vs. Temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ω)')
plt.grid(True)
plt.legend()
plt.show()