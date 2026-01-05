import pandas as pd
import numpy as np
ser = pd.Series(np.random.rand(34))
newdf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# newdf.head()
# newdf.loc[0,0]=654
# print(newdf.head(2))

newdf.columns=list("ABCDE")      #change column no. to ABCDE
# newdf.loc[0,0]=654
# print(newdf.head())      #it will create another column succeding E i.e 0 in which 654 is there

# newdf=newdf.drop(0,axis=1)      #this will remove the column 0
# print(newdf.head()) 

# print(newdf.loc[[1,2],['C','D']])   #it will return the new DF of 1 2 rows and C D columns

# print(newdf.loc[(newdf['A']<0.3)])      #return all values and indexes of column A in which values are < 0.3
# print(newdf.loc[(newdf['A']<0.3)&(newdf['C']>0.1)])       # using & we can add more complex problems in it


####ILOC####
# print(newdf.head())
# print(newdf.iloc[0,4])        #this will gives the value of oth row and 4th index column
# print(newdf.iloc[[0,5],[1,2]])   
# print(newdf.drop([1,5],axis=0, inplace=True))   #drop column

# newdf.head(3)
# print(newdf.reset_index(drop=True))     #start from 0 and drop will remove index column

####isnull####
newdf()
print(newdf['B'].isnull)
