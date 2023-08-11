import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.image as mpimg
from matplotlib.patches import Polygon

def poligonCreate(height):
    # Tabanın altı köşe noktasını belirle (x, y, z) formatında
    base_vertices = np.array([
        [0, 0, 0],  # Nokta A (x, y, z)
        [0, 30, 0],  # Nokta B (x, y, z)
        [10, 30, 0],  # Nokta C (x, y, z)
        [10, 15, 0],  # Nokta D (x, y, z)
        [25, 15, 0],  # Nokta E (x, y, z)
        [25, 0, 0],  # Nokta F (x, y, z)
    ])

    top_vertices = base_vertices + [0, 0, height]

    # Poligonun yüzlerini tanımla
    faces = [
        [base_vertices[0], base_vertices[1], top_vertices[1], top_vertices[0]],  # Alt yüz 1
        [base_vertices[1], base_vertices[2], top_vertices[2], top_vertices[1]],  # Alt yüz 2
        [base_vertices[2], base_vertices[3], top_vertices[3], top_vertices[2]],  # Alt yüz 3
        [base_vertices[3], base_vertices[4], top_vertices[4], top_vertices[3]],  # Alt yüz 4
        [base_vertices[4], base_vertices[5], top_vertices[5], top_vertices[4]],  # Alt yüz 5
        [base_vertices[0], base_vertices[1], base_vertices[2], base_vertices[3], base_vertices[4], base_vertices[5]],
        # Taban yüz
        [top_vertices[0], top_vertices[1], top_vertices[2], top_vertices[3], top_vertices[4], top_vertices[5]],
        # Üst yüz
    ]
    return top_vertices, faces

# Üst yüzün noktalarını belirle (tabanın yüksekliği kadar yukarıda)
height = float(input("Input the height: "))  # Poligonun yüksekliğini belirleyin

# Poligonu ve köşe noktalarını oluştur
top_vertices, faces = poligonCreate(height)

# Eksen oluştur
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Poligonu oluştur
poly3d = [[vertice for vertice in face] for face in faces]  # Köşe noktalarını düzgünce kullan
ax.add_collection3d(Poly3DCollection(poly3d, facecolors='red', linewidths=1, edgecolors='red', alpha=0.2))

# Eksen sınırlarını ayarla
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)
ax.set_zlim(0, 50)

# Cismin yüksekliğini belirleyin
object_height = float(height)

# Güneş yüksekliğini hesaplayın (örneğin 30 derece)
sun_altitude_deg = 45

# Gölge uzunluğunu hesapla
def calculate_shadow_length(sun_altitude_deg, object_height):
    # Güneş ışığının yatay düzlemdeki açısını radyana çevirin
    sun_altitude_rad = np.radians(sun_altitude_deg)

    # Gölge uzunluğunu hesaplayın
    shadow_length = object_height * np.tan(sun_altitude_rad)

    return shadow_length

# Gölge uzunluğunu hesapla
shadow_length = calculate_shadow_length(sun_altitude_deg, object_height)

# Gölgelik oluştur
shadow = Polygon([
    (top_vertices[0][0], top_vertices[0][1]),
    (top_vertices[1][0] - shadow_length, top_vertices[1][1]),
    (top_vertices[2][0] - shadow_length, top_vertices[2][1]),
    (top_vertices[3][0], top_vertices[3][1]),
    (top_vertices[4][0], top_vertices[4][1]),
    (top_vertices[5][0], top_vertices[5][1]),
], closed=True, color='black', alpha=0.5)

# Gölgeyi 2D olarak ekleyin
ax.add_patch(shadow)

# Görselleştirmeyi göster
plt.show()
