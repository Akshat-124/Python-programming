##oops##
#to map the real world scenarios, we started using objects in code.
#class&obj
# class Student:
#     name="akshat"

# s1=Student()     #obj
# print(s1.name)

# s2=Student()
# print(s2.name)

# class Car:
#     color="blue"
#     brand="mercedes"
# car1=Car()
# print(car1.color)
 
##init fuction##

# class Student:
    
#     def __init__(self, name, marks):      #this is constructor which runs whem class is run
#         self.name=name
#         self.marks=marks        #pointing s1 
#         print("adding new student")
# s1=Student("yaksha",99)
# print(s1.name,s1.marks) #yaksha
# s2=Student("raghav",100)         #in result constructor call every time 
# print(s2.name,s2.marks)

##attributes##

# class Student:
#     college_name="ABC clg"      #Attribute
#     name="anonymous"  #class attribute
#     def __init__(self, name, marks):      
#         self.name=name     #obj attribute
#         self.marks=marks         
#         print("adding new student")
# s1=Student("yaksha",99)
# print(s1.name,s1.marks) 
# s2=Student("raghav",100)  
# print(s2.name,s2.marks)
# print(s2.college_name)
# print(Student.college_name)    #class attribute
#print(s1.name)    #yaksha - cuz obj attribute > class attribute

##methods##
#class is collection of attributes(data) and methods
#methods are functions that belongs to obj
# class Student:
#     college_name="ABC clg"      #Attribute
#     name="anonymous"  #class attribute
#     def __init__(self, name, marks):      
#         self.name=name     #obj attribute
#         self.marks=marks  
#     def welcome(self):    #always write self
#         print("welcome",self.name)
#     def get_marks(self):
#         return self.marks
# s1 = Student("yaksha",99)
# s1.welcome()
# print(s1.get_marks())

##lets practice##
# class Students:
#     def __init__(self,name,marks):
#         self.name= name   #obj attribute
#         self.marks = marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your avg score is: ",sum/3)
# s1 = Students("akshat",[99,98,97])
# s1.get_avg()

##static methods##
#methods dont use the self parameter (work at class level)
class Students:
     @staticmethod       #decorator
     def hello():
         print("hello")
     def __init__(self,name,marks):
         self.name= name   #obj attribute
         self.marks = marks
     def get_avg(self):
         sum=0
         for val in self.marks:
             sum+=val
         print("hi",self.name,"your avg score is: ",sum/3)
s1 = Students("akshat",[99,98,97])
s1.get_avg()
s1.hello()

##important

#Abstration## = hiding the imp details of a class and only showing the essential features to the users
#encapsulation## = wrapping data and functions into a single unit(obj).
#lets practice#
class Account:
    def __init__(self,bal,acc):
        self.balance= bal
        self.account_no=acc
        #debit method
        def debit(delf,amount):
            self.balance+=amount
            print("rs",amount,"was credited")
        def get_balance(self):
            return self.balance
acc1=Account(1000,1234)
acc1.debit(1000)
        
