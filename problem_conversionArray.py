import numpy  as np
import os
os.system('cls')

# Fungsi ini astype()membuat salinan array, dan memungkinkan Anda untuk menentukan tipe data sebagai parameter.

arr = np.array([1.1, 2.1, 3.1]) # typenya ini float akan coba di conversi ke integer
convert_int = arr.astype('i') # ini formatnya jika kita ingin conversi array sebelumnya jadi integer..
print(f"{arr} type: {arr.dtype}")
print(f"{convert_int} type: {convert_int.dtype}")
print('-'*100)

# Ubah tipe data dari float ke integer dengan menggunakan intnilai parameter berikut:
floattype = np.array([1.1, 2.1, 3.1]) # typenya ini float akan coba di conversi ke integer
convert_int = floattype.astype(int) # kalau pakai int hasilnya int64
print(f"{floattype} type: {floattype.dtype}")
print(f"{convert_int} type: {convert_int.dtype}")


# Ubah tipe data dari integer menjadi boolean:
print('-'*100)
arr_first = np.array([1, 0, 3])
newarr = arr_first.astype(bool)

print(newarr)
print(newarr.dtype)