import pandas as pd
import numpy as np
ser = pd.Series(np.random.rand(34))
newdf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
newdf.head()
print(type(newdf))
#print(newdf.describe())
# print(newdf)
#print(newdf.index)
#print(newdf.columns)
#print(newdf.to_numpy())      #converted to csv
#print(newdf.T)               #Transpose 

print(newdf.sort_index(axis=0, ascending=False))    #sort in decending order
