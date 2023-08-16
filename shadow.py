import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.image as mpimg

# Kullanıcıdan yükseklik girişi alınır
height = float(input("Yükseklik (m): "))


sun_altitude = math.radians(33)  # Sabit bir yükseklik açısı (90 derece)

if sun_altitude==math.radians(0):
    try:
        print(math.degrees(sun_altitude))
    except ZeroDivisionError:
        # Sıfıra bölme hatası durumunda çalışacak kod bloğu
        print("Please enter a valid number.")
sun_azimuth = math.radians(110)    # Sabit bir azimut açısı (90 derece)


print("Sun altitude:",(math.degrees(sun_altitude)))
print("Sun azimuth:",math.degrees(sun_azimuth))

def calculateShadowLength(height, sun_altitude):
    if sun_altitude == math.radians(90):
        return 0
    if sun_altitude==math.radians(0):
        print("Please enter a valid value")

    shadow_length = height / math.tan(sun_altitude)
    return float(shadow_length)

def calculateShadowWidthAngle(height, shadow_length):
    shadow_width_radians = math.atan2(shadow_length, height)
    shadow_width_angle = math.degrees(shadow_width_radians)
    return shadow_width_angle

# Güneşin yükseklik ve azimut açıları hesaplanır
altitude, azimuth = sun_altitude, sun_azimuth

# Gölge uzunluğu hesaplanır
shadow_length = calculateShadowLength(height, altitude)
print(f"Gölge Uzunluğu: {shadow_length:.2f} m")

# Gölge genişlik açısı hesaplanır
shadow_width_angle = calculateShadowWidthAngle(height, shadow_length)
print(f"Gölge Genişlik Açısı: {shadow_width_angle:.2f} derece")

# Gölge alanı hesaplanır
def calculateShadowArea(height, sun_altitude, shadow_width_angle):
    shadow_area = height * shadow_length * math.tan(sun_altitude + math.radians(shadow_width_angle / 2))
    return shadow_area

shadow_area = calculateShadowArea(height, altitude, shadow_width_angle)
print(f"Gölge Alanı: {shadow_area:.2f} m^2")

def poligonCreate(height, sun_altitude, sun_azimuth):
    # Tabanın altı köşe noktasını belirle (x, y, z) formatında
    base_vertices = np.array([
        [0, 0, 0],    # Nokta A (x, y, z)
        [0, 30, 0],   # Nokta B (x, y, z)
        [10, 30, 0],  # Nokta C (x, y, z)
        [10, 15, 0],  # Nokta D (x, y, z)
        [25, 15, 0],  # Nokta E (x, y, z)
        [25, 0, 0],   # Nokta F (x, y, z)
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

    def calculateShadowStartPoint(base_vertices, shadow_length, sun_altitude, sun_azimuth):
        shadow_start_points = []
        for vertex in base_vertices:
            x, y, z = vertex
            shadow_start_point = [
                x - shadow_length * math.tan(sun_azimuth),
                y - shadow_length * math.tan(sun_altitude),
                z
            ]
            shadow_start_points.append(shadow_start_point)
            print(shadow_start_point)
        return shadow_start_points

    base_vertices_shadow = calculateShadowStartPoint(base_vertices, shadow_length, sun_altitude,sun_azimuth)

    # Gölge yüzeyini tanımla
    faces_shadow = [
        [base_vertices_shadow[0], base_vertices_shadow[1], base_vertices[1], base_vertices[0]],  # Sol yüzey
        [base_vertices_shadow[1], base_vertices_shadow[2], base_vertices[2], base_vertices[1]],  # Ön yüzey
        [base_vertices_shadow[2], base_vertices_shadow[3], base_vertices[3], base_vertices[2]],  # Sağ yüzey
        [base_vertices_shadow[3], base_vertices_shadow[4], base_vertices[4], base_vertices[3]],  # Arka yüzey
        [base_vertices_shadow[4], base_vertices_shadow[5], base_vertices[5], base_vertices[4]],  # Alt yüzey
    ]

    # Eksen oluştur
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.view_init(elev=90,azim=-90)

    poly2d = [[vertice for vertice in face] for face in faces_shadow]  # Köşe noktalarını düzgünce kullan
    ax.add_collection3d(Poly3DCollection(poly2d, facecolors='black', linewidths=1, edgecolors='gray', alpha=0.2))

    # Poligonu oluştur
    poly3d = [[vertice for vertice in face] for face in faces]  # Köşe noktalarını düzgünce kullan
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='red', linewidths=1, edgecolors='red', alpha=0.5))

    # Eksen sınırlarını ayarla
    ax.set_xlim(-60, 60)
    ax.set_ylim(-60, 60)
    ax.set_zlim(0, 50)

    # Güneş resmini yükleyin
    sun_img = mpimg.imread('sun.png')

    # Güneşi sahne dışına eklemek için yeni bir subplot oluşturun
    ax2 = fig.add_axes([0.5, 0.8, 0.2, 0.2], zorder=1)
    ax2.imshow(sun_img, alpha=0.5)  # alpha saydamlığı belirler (0-1 arasında olmalı)
    ax2.axis('off')  # Eksenleri kapat



    plt.show()

poligonCreate(height, sun_altitude, sun_azimuth)

