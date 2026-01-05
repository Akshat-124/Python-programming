import numpy as np
import pandas as pd
# dict1 = {
#     "name":['akshat','yaksha','raghav'],
#     "marks":[95,97,100],
#     "city":["sonipat","sonipat","sonipat"]
# }
# df=pd.DataFrame(dict1)
# print(df)
# df.to_csv('friends.csv')  #convert data to csv file (excle sheet)
# df.to_csv('friends_index_false.csv',index=False) #remove index from csv
akshat=pd.read_csv('pandas/akshat.csv')
print(akshat)
print(akshat['speed'])
akshat['speed'][0]=50
print(akshat)
akshat.to_csv('akshat.csv')