import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.image as mpimg



# Üst yüzün noktalarını belirle (tabanın yüksekliği kadar yukarıda)
height = input("İnput the height: ")  # Poligonun yüksekliğini belirleyin


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

    # Güneş resmini yükleyin
    sun_img = mpimg.imread('sun.png')



    # Güneşi sahne dışına eklemek için yeni bir subplot oluşturun
    ax2 = fig.add_axes([0.5, 0.8, 0.2, 0.2], zorder=1)
    ax2.imshow(sun_img, alpha=0.5) #alpha saydamlığı belirler 0-1 arasında olmalı
    ax2.axis('off')  # Eksenleri kapa



    # Görselleştirmeyi göster
    plt.show()






poligonCreate(int(height))