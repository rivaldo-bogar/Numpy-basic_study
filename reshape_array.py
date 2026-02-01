# Function shape untuk mengetahui berapa baris dan berapa kolom pada  suatu array.
import numpy as np
import os
os.system('cls')

global arr,arrtwo
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) #contohnya 0,1 = 2 baris ada 4 angkat
arrtwo = np.array([1, 2, 3, 4, 5, 6, 7, 8])


def reshape_array2D():
    new_reshape = arr.reshape(4,3) # jika angkanya tidak seimbang jumlah array akan error
    '''
    Fungsi .reshape(4, 3) digunakan untuk mengubah struktur dimensi data tanpa menambah atau mengurangi isinya. Dalam kasus ini, kamu mengubah barisan 12 angka menjadi bentuk tabel yang terdiri dari 4 baris dan 3 kolom.
    '''
    print(f'{new_reshape}') 
def reshape_array3D():
    #Reshape From 1-D to 3-D
    new_rshep = arr.reshape(2, 3, 2)
    print(new_rshep)
def check_base():
    text = """
    Kesimpulannya reshape tidak menghasilkan duplicate atau copy,jika kita cek dengan
    base kalau hasilnya None berarti bukan dari data asli
"""
    print(text)
    print(arrtwo.reshape(2, 4).base)

def hitung_otomatis():
    otomat = arr.reshape(2,-1) # menghitung otomatis shape
    print(otomat)

if __name__ == '__main__':

    # reshape_array2D()
    # reshape_array3D()
    # check_base()
    hitung_otomatis()