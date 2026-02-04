import numpy as np
import os
os.system('cls')

def WorkWith_Concatenate():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    # Menggabungkan arr1 dan arr2 menjadi satu array baru tanpa menambah dimensi baru (tetap 1D).
    # np.concatenate membuat copy baru di memori.Hati hati jika databesar
    arr = np.concatenate((arr1, arr2))
    print(arr)


def WorkWith_AxisHorizontal():
    # Arah: axis=1 berarti penggabungan dilakukan pada sumbu horizontal.
    # axis=0 vertical,silahkan dicoba running
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    arr = np.concatenate((arr1, arr2), axis=1)
    print(arr)
    
def WorkWith_stack():
    # Menggabungkan dua array 1D menjadi satu matriks 2D dengan cara memasangkan elemen berdasarkan indeksnya (transformasi dari vektor ke kolom).
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.stack((arr1, arr2), axis=1)
    print(arr)

def WorkWith_hstack():
    # Secara performa dan hasil, untuk array 1D, hstack sama dengan concatenate default. Namun, hstack lebih "aman" secara semantik jika kamu ingin memastikan penggabungan selalu terjadi pada kolom (horizontal) tanpa peduli inputnya 1D atau 2D.

    # Menggabungkan array secara mendatar (horizontal).
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.hstack((arr1, arr2))
    print(arr)
     
def WorkWith_vstack():
    # Fungsi: Menumpuk array secara vertikal untuk membentuk matriks baru.
    # Perilaku: Mengubah dua array 1D menjadi matriks 2D di mana setiap array asal menjadi satu baris.

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.vstack((arr1, arr2))
    print(arr)

def WorkWith_dstack():
    #Fungsi: Menggabungkan array di sepanjang sumbu ketiga (axis=2).
    # Perilaku: Mengubah array 1D (vektor) langsung menjadi array 3D. Elemen dengan indeks yang sama dipasangkan di baris dan kolom yang sama, namun dipisahkan oleh "kedalaman".
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.dstack((arr1, arr2))
    print(arr) 


if __name__ == '__main__':
    # WorkWith_Concatenate()
    # # print('-'*100)
    # # WorkWith_AxisHorizontal()
    # # print('-'*100)
    # # WorkWith_stack()
    # print('-'*100)
    # WorkWith_vstack()
    print('-'*100)
    WorkWith_dstack()
