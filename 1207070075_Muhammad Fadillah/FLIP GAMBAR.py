import numpy as np                                # Import library numpy untuk manipulasi array
import imageio.v2                                 # Import library imageio untuk membaca dan menulis gambar
import matplotlib.pyplot as plt                  # Import library matplotlib untuk plotting

img = imageio.v2.imread("GAMBAR/GTR-R35.jpg")       # Membaca gambar GTR-R35.jpg ke dalam variabel img
img_height = img.shape[0]                         # Mendapatkan ukuran tinggi gambar dalam piksel
img_width = img.shape[1]                          # Mendapatkan ukuran lebar gambar dalam piksel
img_channel = img.shape[2]                        # Mendapatkan jumlah channel dalam gambar
img_type = img.dtype                              # Mendapatkan tipe data dari gambar

img_flip_horizontal = np.zeros(img.shape, img_type)   # Membuat array kosong dengan ukuran yang sama dengan gambar
img_flip_vertical = np.zeros(img.shape, img_type)     # Membuat array kosong dengan ukuran yang sama dengan gambar

# Melakukan flipping horizontal pada gambar
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]

# Melakukan flipping vertical pada gambar
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c] 

fig, axes = plt.subplots(1, 2, figsize=(10, 10))     # Membuat plot 2 gambar dengan ukuran 10 x 10
ax = axes.ravel()                                   # Melakukan plotting pada masing-masing gambar
ax[0].imshow(img_flip_horizontal, cmap='gray')      # Menampilkan gambar hasil flipping horizontal
ax[0].set_title("Flip Horizontal")                  # Memberikan judul pada gambar hasil flipping horizontal
ax[1].imshow(img_flip_vertical, cmap='gray')        # Menampilkan gambar hasil flipping vertical
ax[1].set_title("Flip Vertical")                    # Memberikan judul pada gambar hasil flipping vertical
fig.tight_layout()                                  # Menyesuaikan tata letak gambar
plt.show()                                          # Menampilkan plot gambar

