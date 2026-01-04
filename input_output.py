# open read &close file
# f=open("file_name","mode")
f=open("demo.txt","r")
data= f.read(5)      #print starting 5 elements
print(data)
print(type(data))
f.close( )

#line1 = f.readline()            print 1st line 
#print(line1)           
#line2 = f.readline()            print 2nd line
#print(line2)  
# f.close()         

##WRITING TO A FILE##
# f=open("file_name","mode")
# f=open("file_name","w")
f=open("demo.txt","w")           #wrie in demo.txt  
f.write("i have learned")

f=open("demo.txt","a")           #append/add in demo.txt  
f.write("\nafter that nodejs")
f.close()
# if we are using write mode w in code and then the txt file is not exists python will automatically create a new file

f=open("demo.txt","r+")        #this is for overwrite in file and also we read the file
f.write("ABC")
f.close()

##With syntax##
with open("demo.txt", "r") as f:          #as is an alias
       data=f.read()
       print(data)
#using with syn we dont need to close the file cuz with syn automatically close the file

##DELETING a file##
# import os
# os.remove(filename) #through this we can remove a file

#lets practice
with open ("practice.txt","r") as f:
       data=f.read()
new_data = data.replace("java","python")
print(new_data)
with open("practice.txt","w") as f:
       f.write(new_data)
       