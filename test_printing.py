import numpy as np # np adalah alias dari numpy,jika kita menggunakan as

data = np.array([12,23,22,11,23,44]) # contoh list dalam bentuk numpy
dic = np.array((2,1,22,11,23,44)) # contoh list dalam bentuk numpy
print(f'{data} type: {type(data)}')
print(f'{dic} type: {type(dic)}')
print(np.__version__) # cek version
