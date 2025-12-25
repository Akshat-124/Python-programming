str1 = "this is a string \n we r creating it in py"
 #same goes for'' " " "' "'
print(str1)

#concatination-"hello" + "world"
str1 = "apna"
print(len(str1))
str2 = "college"
print(len(str2))
finalstring =str1+str2
print(finalstring)
print(len(finalstring))

#indexing
#indexing doesnt modify the char
str="akshat"
ch=str[1]
print(ch)

#slicing=accessing parts of a string
str="apna college"
print(str[1:4])
print(str[5:7])
print(str[5:])
print(str[:5])

#strings functions
str="i am a coder"
print(str.endswith("er"))
print(str.capitalize())
print(str.replace("coder","good coder"))
print(str.find("a")) #returns index of "a"

# #lets practice
# #wap input name and cal len
# name=input("enter your name: ")
# print(len(name))
# #wap to find occurrence of $ in a string
# str="hi i am $ and my value is $99.99"
# print("occurence of $ here is: " ,str.count("$") )

#conditional statements
age=22
if (age >=18):
    print("elegible to vote")

light="green"
if(light == "green"):
    print("go")
elif(light=="yellow"):
    print("look")
elif(light=="red"):
    print("stop")