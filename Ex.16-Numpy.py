#Exercícios Numpy-16
#*******************

import numpy as np

arr=np.ones((10,10))

arr_b=np.pad(arr,pad_width=1, mode ='constant',constant_values=0)

print(arr_b)

