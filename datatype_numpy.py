import numpy as np
import os

arr = np.array([1, 2, 3, 4]) # int64

str_arr = np.array(['apple', 'banana', 'cherry']) #string unicode
os.system('cls')

# Dapatkan tipe data dari objek array: (menggunakan dtype untuk kita mengetahui type data value dari array..)
print(arr.dtype) # int64
print(str_arr.dtype) #string unicode

print("-" * 50)

# Membuat Array dengan Tipe Data yang Terdefinisi
'''
1. Apa itu Awalan b?
Huruf b di depan angka (b'1') artinya data tersebut disimpan sebagai Byte String, bukan string Unicode biasa.

String biasa: '1' (bisa menyimpan karakter aneh/emoji).

Byte string: b'1' (lebih hemat memori, hanya karakter dasar ASCII).

2. Apa itu |S1?
Itu adalah dtype (data type) dari array kamu:

S: Artinya "String" (lebih tepatnya zero-terminated bytes).

1: Artinya panjang maksimal karakter di tiap elemen adalah 1. Jadi kalau kamu masukkan kata "Halo", dia cuma bakal ambil huruf "H" saja.

|: Simbol endianness (tidak perlu terlalu dipikirkan untuk sekarang).
'''
arrayset_type = np.array([1, 2, 3, 4], dtype='S')
print(arrayset_type)
print(arrayset_type.dtype) #string unicode

print("-" * 50)

# Buat array dengan tipe data integer 4 byte:
intbyte = np.array([1, 2, 3, 4], dtype='i4')
print(intbyte)
print(intbyte.dtype) # ingat 32 itu bit,karena 1 byte = 8 bit.