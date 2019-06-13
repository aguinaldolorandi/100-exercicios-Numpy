#Exercícios Numpy-13
#*******************

import numpy as np

np.random.seed(100)

np.set_printoptions(precision=3)

arr=np.random.random([10,10])

arrMax,arrMin=arr.max(),arr.min()

print(arrMax)
print(arrMin)

