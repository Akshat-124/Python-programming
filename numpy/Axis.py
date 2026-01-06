import numpy as np
x=[[1,2,3],[4,5,6],[7,1,0]]
ar=np.array(x)
print(ar)
sum0=ar.sum(axis=0)      #prints col wise sum
print(sum0)
sum1=ar.sum(axis=1)      #prints rows wise sum
print(sum1)
transpose=ar.T
print(transpose)         #create transpose matrix
space=ar.nbytes          #space occupy
print(space)       
dim=ar.ndim              #no. of dimensions
print(dim)
size=ar.size             #total elements in array
print(size)
##more ops

one=np.array([1,3,4,634,2])
max=one.argmax()           #returns index of max element
print(max)
min=one.argmin()
print(min)
sort=one.argsort()         #srt array in ascending order
print(sort)
 
##in 2d array

print(ar)
max1=ar.argmax()
print(max1)
sort0=ar.argsort(axis=0)    #sort cols in a ascending way
print(sort0 )




