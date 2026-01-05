import numpy as np
ar2=np.array([[1,2,1],[4,0,6],[8,1,0]])
ar=np.array([[1,2,3],[4,5,6],[7,1,0]])
sum=ar+ar2
print(sum)                    #add elementwise sum
sqrt=np.sqrt(ar2)             #sqrt of array
print(sqrt)
max=ar.max()                  #max element in array
min=ar.min()
print(max)
print(min)
find=np.where(ar>5)            #find elements which is > 5 in array
count=np.count_nonzero(ar)     #count non0 elements in aray
print(find)
print(count)