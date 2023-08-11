import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.image as mpimg

# Üst yüzün noktalarını belirle (tabanın yüksekliği kadar yukarıda)
height = int(input("İnput the height: "))  # Poligonun yüksekliğini belirleyin

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

    # Poligonun yüzlerini tanımla (aynı şekilde devam eder)

    # Eksen oluştur
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Poligonu oluştur (aynı şekilde devam eder)

    # Güneş resmini yükleyin
    sun_img = mpimg.imread('sun.png')  # 'sun.png' dosya adını güneş resminin dosya adıyla değiştirin

    # Güneşi ekrana ekleyin
    ax.imshow(sun_img, extent=(0, 50, 0, 50, 0, 50), alpha=0.5)  # (x_min, x_max, y_min, y_max, z_min, z_max)

    # Eksen sınırlarını ayarla
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_zlim(0, 50)

    # Görselleştirmeyi göster
    plt.show()

poligonCreate(height)
