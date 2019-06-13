# Exercícios Numpy-34
# *******************
import numpy as np

#((A+B)*(-A/2)

A=np.ones((3,3))*1
B=np.ones((3,3))*2

resultado=((A+B))

print(np.add(A,B))
print(np.divide(A,2,out=A))
print(np.multiply(A,B))

print(resultado)