# Exercícios Numpy-30
# *******************
import numpy as np

a=np.arange(10,26).reshape(4,-1)

b=np.arange(1,17).reshape(4,-1)

print(a)
print(b)

print(np.intersect1d(a,b))

