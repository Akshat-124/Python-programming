name = "akshat" #string
age = 23
price =25.99

age2 = age

print(name,age,price)
print(age2)
print("my name is: ",name)

#  identifiers=1.identi. cannot start with digit. so while var1 is valid,1var is not.
#  2.we cant use special symb like !@#$%& etc in identi.
#  3. identi. can be of any len.

print(type(name))
print(type(age))
print(type(price))

##DataTypes=int,str(" "),float,bool(true,false),none

age=23
old=False
a=None
print(type(old))
print(type(a))

# operators=perform operands
# arithmetic ops-
a=5
b=2
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a**b)
#relational ops-
a=50
b=20
print(a==b) #false
print(a!=b) #true
print(a>=b) 
print(a<=b) 
# assignment ops-
a=50 #=is ass op
num=10
num+=10 #10+10=20 same for *,-,/,**
print("num : ",num)
# logical ops-
print(not False)
print(not True)
val1=True
val2=False
print("ans op: ",val1 and val2)
print("ans op: ",val1 or val2)

#Type conversion-
a=2
b=4.25
print(a+b) #2.0+4.25=6.25

a=int("2")
b=4.25
print(a+b) #this method of coverting string to int forcefully is called casting cuz u cannot add float to str .

# input in pyt -
# input("enter your name: ")
# print("welcome: ",name)

# lets practice-

# a=int(input("enter the 1st no: "))
# b=int(input("enter the 2nd no: "))
# sum = a + b
# print (sum)

# a=float(input("side of square is: "))
# area=a**2
# print("area of sq is: ",area)

# a=float(input("enter 1st no.: "))
# b=float(input("enter 2md value:"))
# avg=(a+b)/2
# print("avg of two float values is: ",avg)