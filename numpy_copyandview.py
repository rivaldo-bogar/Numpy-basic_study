import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() # mencopy sehingga membuat array baru,tidak ada keterkaitan dengan array sebelumnya.
arr[0] = 42  # mencoba mengubah nilai pada array variabel arr.

print(arr)
print(x)
# kedua output ini berbeda karena sudah dicopy..