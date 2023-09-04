import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def update_plot(*args):
    ax.clear()

    # Güneş açılarını al
    sun_azimuth = math.radians(azimuth_scale.get())
    sun_elevation = math.radians(elevation_scale.get())

    # Güneş yön vektörünü hesapla
    sun_vector_x = math.cos(sun_azimuth) * math.cos(sun_elevation)
    sun_vector_y = math.sin(sun_azimuth) * math.cos(sun_elevation)
    sun_vector_z = math.sin(sun_elevation)


    shadow_length = object_height * math.tan(math.radians(90-elevation_scale.get()))
    print(shadow_length)
    # Cismin gölge noktalarını hesapla
    shadow_vertices = []
    for vertex in polygon_vertices:
        shadow_x = vertex[0] - object_height - shadow_length / sun_vector_z * sun_vector_x
        shadow_y = vertex[1] - object_height - shadow_length / sun_vector_z * sun_vector_y
        shadow_z = 0  # Gölgenin z koordinatını sıfır olarak ayarla
        shadow_vertices.append([shadow_x, shadow_y, shadow_z])
    print(shadow_vertices)
    # Gölge noktalarını ve poligon noktalarını çizgiyle birleştir
    lines = []
    surfaces = []  # Yüzeylerin köşe noktalarını saklamak için
    for i in range(len(shadow_vertices)):
        line = np.array([[shadow_vertices[i][0], shadow_vertices[i][1], shadow_vertices[i][2]],
                         [polygon_vertices[i][0], polygon_vertices[i][1], polygon_vertices[i][2]]])
        lines.append(line)
        surfaces.append([shadow_vertices[i], polygon_vertices[i], polygon_vertices[(i + 1) % len(polygon_vertices)],
                         shadow_vertices[(i + 1) % len(shadow_vertices)]])
    # Gölge noktaları arasındaki çizgileri çiz
    for i in range(len(shadow_vertices) - 1):
        line = np.array([[shadow_vertices[i][0], shadow_vertices[i][1], shadow_vertices[i][2]],
                         [shadow_vertices[i + 1][0], shadow_vertices[i + 1][1], shadow_vertices[i + 1][2]]])
        lines.append(line)
        surfaces.append([shadow_vertices[i], shadow_vertices[i + 1], polygon_vertices[i + 1], polygon_vertices[i]])
    line_collection = Line3DCollection(lines, colors='gray')
    ax.add_collection3d(line_collection)
    # Yüzeyleri gri renkle çiz
    surfaces_collection = Poly3DCollection(surfaces, facecolors='gray', edgecolors='gray', alpha=0.5)
    ax.add_collection3d(surfaces_collection)
    # ... (Çizim işlemlerini burada güncelle) ...
    # Poligonu oluştur
    poly3d = [[vertice for vertice in face] for face in faces]  # Köşe noktalarını düzgünce kullan
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='red', linewidths=1, edgecolors='red', alpha=0.5))
    # Gölge noktalarını çiz
    shadow_vertices = np.array(shadow_vertices)
    ax.scatter(shadow_vertices[:, 0], shadow_vertices[:, 1], shadow_vertices[:, 2], color='gray', marker='o')
    ax.set_xlim(-60, 60)
    ax.set_ylim(-60, 60)
    ax.set_zlim(0, 50)
    canvas.draw()

object_height = float(input("Enter object height: "))
object_height = int(object_height)


polygon_vertices = np.array([
    [0, 0, 0],
    [0, 30, 0],
    [10, 30, 0],
    [10, 15, 0],
    [25, 15, 0],
    [25, 0, 0],
    [0,0,0]
])
top_vertices = polygon_vertices + [0, 0, float(object_height)]
# Poligonun yüzlerini tanımla
faces = [
        [polygon_vertices[0], polygon_vertices[1], top_vertices[1], top_vertices[0]],  # Alt yüz 1
        [polygon_vertices[1], polygon_vertices[2], top_vertices[2], top_vertices[1]],  # Alt yüz 2
        [polygon_vertices[2], polygon_vertices[3], top_vertices[3], top_vertices[2]],  # Alt yüz 3
        [polygon_vertices[3], polygon_vertices[4], top_vertices[4], top_vertices[3]],  # Alt yüz 4
        [polygon_vertices[4], polygon_vertices[5], top_vertices[5], top_vertices[4]],  # Alt yüz 5
        [polygon_vertices[0], polygon_vertices[1], polygon_vertices[2], polygon_vertices[3], polygon_vertices[4], polygon_vertices[5]], # Taban yüz
        [top_vertices[0], top_vertices[1], top_vertices[2], top_vertices[3], top_vertices[4], top_vertices[5]], # Üst yüz
]


# Tkinter penceresini oluştur
root = tk.Tk()
root.title("3D Çizim")

# Scale widget'ları oluştur
azimuth_scale = tk.Scale(root, label="Sun Azimuth", from_=0, to=180, orient="horizontal")
elevation_scale = tk.Scale(root, label="Sun Elevation", from_=1, to=89, orient="horizontal")

# Çizim için matplotlib FigureCanvasTkAgg oluştur
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-60, 60)
ax.set_ylim(-60, 60)
ax.set_zlim(0, 50)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

# Scale değerleri değiştiğinde çizimi güncelle
azimuth_scale.bind("<Motion>", update_plot)
elevation_scale.bind("<Motion>", update_plot)

# Scale widget'larını grid ile yerleştir
azimuth_scale.grid(row=0, column=0, padx=10, pady=10)
elevation_scale.grid(row=0, column=1, padx=10, pady=10)

# Canvas'ı grid ile yerleştir
canvas_widget.grid(row=1, column=0, columnspan=2)

# Tkinter penceresini başlat
root.mainloop()