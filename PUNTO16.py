import matplotlib.pyplot as plt

def dibujar_letra(ax, coords, offset_x=0, offset_y=0, color="blue"):
    """Dibuja una letra usando coordenadas de segmentos"""
    for seg in coords:
        x = [p[0] + offset_x for p in seg]
        y = [p[1] + offset_y for p in seg]
        ax.plot(x, y, color=color, linewidth=2)

letras = {
    "E": [[(0,0),(0,5)], [(0,5),(3,5)], [(0,2.5),(2,2.5)], [(0,0),(3,0)]],
    "M": [[(0,0),(0,5)], [(0,5),(1.5,2.5)], [(1.5,2.5),(3,5)], [(3,5),(3,0)]],
    "R": [[(0,0),(0,5)], [(0,5),(2.5,5)], [(2.5,5),(2.5,2.5)], [(0,2.5),(2.5,2.5)], [(0,2.5),(3,0)]],
    "S": [[(3,5),(0,5)], [(0,5),(0,2.5)], [(0,2.5),(3,2.5)], [(3,2.5),(3,0)], [(3,0),(0,0)]],
    "O": [[(0,0),(0,5)], [(0,5),(3,5)], [(3,5),(3,0)], [(3,0),(0,0)]],
    "N": [[(0,0),(0,5)], [(0,5),(3,0)], [(3,0),(3,5)]],
    "I": [[(0,0),(3,0)], [(1.5,0),(1.5,5)], [(0,5),(3,5)]],
    "C": [[(3,5),(0,5)], [(0,5),(0,0)], [(0,0),(3,0)]],
    "L": [[(0,5),(0,0)], [(0,0),(3,0)]],
}

fig, ax = plt.subplots(figsize=(12,6))

offset_x = 0
for letra in "EMERSON":
    dibujar_letra(ax, letras[letra], offset_x=offset_x, offset_y=6, color="blue")
    offset_x += 5 

offset_x = 0
for letra in "NICOL":
    dibujar_letra(ax, letras[letra], offset_x=offset_x, offset_y=0, color="red")
    offset_x += 5

ax.set_aspect('equal')
ax.axis("off")
plt.title("Nombres integrantes")
plt.show()
