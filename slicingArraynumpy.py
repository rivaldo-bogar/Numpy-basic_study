import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# start ambil dari 2 3 4 5 (ingat index di hitung dari 0)
print(arr[1:5])
# mengambil dari index 4 hingga akhir..
print(arr[4:])
# Iris elemen dari awal hingga indeks 4 (tidak termasuk) || maksudnya index ke 4 tidak di tampilkan
print(arr[:4])