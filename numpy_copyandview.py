import numpy as np
import os

def copy_arry():
    os.system('cls')
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy() # mencopy sehingga membuat array baru,tidak ada keterkaitan dengan array sebelumnya.
    arr[0] = 42  # mencoba mengubah nilai pada array variabel arr.
    print("NUMPY -- COPY")
    print(arr)
    print(x)
    print('-'*100)
    return arr
    
def view_numpy(turunanarr):
    print("NUMPY -- VIEW")
    a = turunanarr.view()
    print(turunanarr)
    print(a)
def cek_dataarray(myarray):
    print("NUMPY -- CEK")
    testcopy = myarray.copy()
    testview = myarray.view()
    # Apakah kamu pemilik asli data ini, atau kamu cuma meminjam (melihat) dari array lain?
    print(testcopy.base)
    print(testview.base)
    pass
# standar international
if __name__ == '__main__':
    cekdata = copy_arry() 
    numpy_arr = copy_arry()
    # copy_arry()
    cek_dataarray(cekdata)
    # view_numpy(numpy_arr)



# kedua output ini berbeda karena sudah dicopy..