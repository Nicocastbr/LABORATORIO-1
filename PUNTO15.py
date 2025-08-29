import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, x, y, z, color='blue', arrow_length_ratio=0.1, linewidth=2)

ax.set_xlim([min(0, x)-1, max(0, x)+1])
ax.set_ylim([min(0, y)-1, max(0, y)+1])
ax.set_zlim([min(0, z)-1, max(0, z)+1])

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Vector en coordenadas 3D")

ax.grid(True)
plt.show()
