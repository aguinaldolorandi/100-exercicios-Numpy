# Exercícios Numpy-33
# *******************
import numpy as np
import datetime




data_hoje=np.datetime64('today','D')

data_ontem=data_hoje+np.timedelta64(-1,"D")

data_amanhã=data_hoje+np.timedelta64(1,'D')

print(data_hoje)
print(data_ontem)
print(data_amanhã)



