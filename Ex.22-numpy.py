# Exercícios Numpy-22
# *******************
import numpy as np

np.set_printoptions(precision=3)

z=np.random.random((5,5))

Zmin,Zmax=z.min(),z.max()

Z=z-Zmin/(Zmax-Zmin)

print(Z)


