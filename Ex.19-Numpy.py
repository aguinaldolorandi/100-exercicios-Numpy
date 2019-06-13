# Exercícios Numpy-19
# *******************

import numpy as np


b = np.zeros((8, 8),dtype=int)

b[1::2,0::2]=1
b[0::2,1::2]=1



print(b)

