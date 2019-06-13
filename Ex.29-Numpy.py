# Exercícios Numpy-29
# *******************
import numpy as np

#np.set_printoptions(precision=0)

arr=np.random.random((5,5))

print(arr)
print()

Z = np.random.uniform(-10,+10,10)

print()
print(Z)
print(np.ceil(Z))
print (np.ceil(np.abs(Z)))
print (np.copysign(np.ceil(np.abs(Z)), Z))