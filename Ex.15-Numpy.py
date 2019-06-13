#Exercícios Numpy-15
#*******************

import numpy as np

arr=np.ones((10,10))

arr[1:-1,1:-1]=0

print(arr)
print()

arr_zero=np.zeros((8,8))

arr_zero=np.pad(arr_zero,pad_width=1,mode='constant',constant_values=1)
print(arr_zero)