import numpy as np
import os
os.system('cls')
global treearray,two
two = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
treearray = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 111]]])

def iterasi_nditertest():
    for x in np.nditer(treearray): # looping dengan singkat tanpa perlu bercabang seperti for loop dalam loop
        print(x,x.dtype)
        
def nditer_convert():
    for x in np.nditer(treearray,flags=['buffered'], op_dtypes=['S']):
        print(f"{x} {x.dtype}")

def nditer_skalar():
    '''
    Berikut penjelasannya dibawah ini.
    : (Kiri): Artinya "Ambil semua baris" (Jangan ada baris yang ditinggal).
    ::2 (Kanan): Artinya "Mulai dari awal, jalan sampai ujung, tapi langkahnya loncat 2".

    Baris 1: [1, 2, 3, 4]  --> Ambil 1, loncat 2, ambil 3. (Hasil: 1, 3)
    Baris 2: [5, 6, 7, 8]  --> Ambil 5, loncat 6, ambil 7. (Hasil: 5, 7)
    '''
    print(two)
    for x in np.nditer(two[:, ::2]):
        print(x)

def Iterasi_terenumerasi():
    # mencari tahu baris dan kolom dari suatu value (nil_baris,nil_kolom)
    for idex,x in np.ndenumerate(two):
        print(f"{idex} -----> {x}")
    
if __name__ == '__main__':
    iterasi_nditertest()
    print('-'*100)
    nditer_convert()
    print('-'*100)
    nditer_skalar()
    print('-'*100)
    Iterasi_terenumerasi()