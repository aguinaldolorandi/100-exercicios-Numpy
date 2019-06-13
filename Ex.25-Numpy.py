# Exercícios Numpy-25
# *******************
import numpy as np

Z=np.arange(12)

print(Z)

Z[3:9]=0
print(Z)

Z = np.arange(11)
Z[(Z>=3) & (Z<=8)] *= -1
print(Z)