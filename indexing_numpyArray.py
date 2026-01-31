import numpy as np

# Array 1 dimensi
arr = np.array([1, 2, 3, 4])
# array 2 dimensi
twodimen = np.array([[1,2,3,4,5], [6,7,8,9,15]])

# Array 3 dimensi
treedimen = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# memanggil index pada array
print(arr[2])

# Mengambil array ke 3 dari arr dan array ke 4 lalu dijumlahkan..
print(arr[2] + arr[3])
# Mencetak element terakhir pada array 2dimensi
print(f"last element {twodimen[1,-1]}")
# Mengakses baris kedua kolom ke empat,ingat hitungannya dari 0,1,2,3,4...
'''
[1,2,3,4,5]
[6,7,8,9,10]
'''
# di atas konsepnya jika saya susun biar mudah dipahami valdo..
print('2nd element on 1st row: ', twodimen[1, 4])

print(treedimen[0, 1, 2]) # penjelasannya dibawah,tapi terakhir saya sudah mengerti cara bacanya..
'''
arr[0, 1, 2]mencetak nilai tersebut 6.

Dan inilah alasannya:

Angka pertama mewakili dimensi pertama, yang berisi dua array:
[[1, 2, 3], [4, 5, 6]]
dan:
[[7, 8, 9], [10, 11, 12]]
Karena kita memilih 0, maka kita tinggal memiliki array pertama:
[[1, 2, 3], [4, 5, 6]]

Angka kedua mewakili dimensi kedua, yang juga berisi dua larik:
[1, 2, 3]
dan:
[4, 5, 6]
Karena kita memilih 1, maka kita mendapatkan larik kedua:
[4, 5, 6]

Angka ketiga mewakili dimensi ketiga, yang berisi tiga nilai:
4
5
6
Karena kita memilih 2, kita mendapatkan nilai ketiga:
6
'''