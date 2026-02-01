# Function shape untuk mengetahui berapa baris dan berapa kolom pada  suatu array.
import numpy as np
import os
os.system('cls')

global arr,arr_another
arr_another = np.array([1, 2, 3, 4], ndmin=5) # nilainya tetap sama tapi ada 5 dimensi
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) #contohnya 0,1 = 2 baris ada 4 angkat
'''
[1, 2, 3, 4]
[5, 6, 7, 8]

2 baris 4 kolom
'''
def check_arraySize():
    print(arr.shape)

def array_manydimen():
    print(f'{arr_another.shape}') 

if __name__ == '__main__':
    check_arraySize()
    array_manydimen()