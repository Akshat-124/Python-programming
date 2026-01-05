import numpy as np
zeros = np.zeros((2,5))    #creats 2 rows and 5 cols of 0s
print(zeros)
rng = np.arange(15)    # 1d array from 0 to 14
print(rng)
lspace=np.linspace(1,5,12)   # random 12 values from 1 to 5
print(lspace)
emp = np.empty((4,6))
print(emp)
ide = np.identity(45)   #identity matrix
print(ide)
print(ide.shape)

##different fns of numpy
arr= np.arange(99)
print(arr)
reshape=arr.reshape(3,33)     #3 arrays of 33 elements each
print(reshape)
ravel= arr.ravel()            #creates a 1d array
print(ravel)