import numpy as np

# array 0D --- 0 dimensi
zerodimen = np.array(13)
# 1D -- 1 dimensi
onedimen = np.array([2,2,1,2])
# 2D -- 2 dimensi
twodimen = np.array([[2,2,1,2],[5,5,1,4]])
# 3D -- 3 dimensi
treedimen = np.array([[[2,2,1,2],[5,5,1,4]],[[2,2,1,2],[5,5,1,4]]])
# 5D -- 5 dimensi
fivedimen = np.array([2,2,1,2],ndmin=5) # kali ini kita tentukan dimensinya

# fungsi ndim --> memberitahu kita berapa dimensi array tersebut..
print(f"numpy-array 0D = {zerodimen.ndim}")
print(f"numpy-array 1D = {onedimen.ndim}")
print(f"numpy-array 2D = {twodimen.ndim}")
print(f"numpy-array 3D = {treedimen.ndim}")
print(f"numpy-array 5D = {fivedimen.ndim}")