import numpy as np
import os
os.system('cls')
global arr,twoarray,treearray
arr = np.array([1, 2, 3, 4])
twoarray = np.array([[1, 2, 3], [4, 5, 6]])
treearray = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

def iterasi_numpy():
    for x in arr:
        print(x)
def iterasi_twoarray():
    for x in twoarray:
        for y in x:
            print(y)

def iterasi_treedimen():
    for x in treearray:
        for y in x: # jika ingin tampilkan bentuk array : singkat saja print(x)
            for z in y:
                print(z)
    
    

if __name__ == '__main__':
    # iterasi_numpy()
    # iterasi_twoarray()
    iterasi_treedimen()