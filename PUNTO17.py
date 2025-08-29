import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title="Seleccione el logo",
    filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.bmp")]
)

img = cv2.imread(file_path)

if img is None:
    print("⚠️ Error: No se pudo cargar la imagen.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0,255,0), 2)

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Imagen original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB))
plt.title("Contornos detectados")
plt.axis("off")

plt.show()
