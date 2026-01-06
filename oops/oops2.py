#delete
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("Akshat")
# print(s1.name)                             #prints the name
# del s1.name          #del the name
# print(s1.name)                             #returns error because name is deleted

#private attributes
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
# acc1=Account("1234","abcd")
# print(acc1.acc_no)                        #this will print the acc no 
# print(acc1.__acc_pass)                    #this retun error because acc_pass is private    

# class Person:
#     __name="anonymous"
#     def __hello(self):
#         print("hello person!")
#     def welcome(self):
#         self.__hello()                       #these private attributes are being accessed within the class not from outside
# p1=Person()
# print(p1.welcome)       

##inheritance## = when one class(child/derived) derives the prop & method of another class(parent/base)
# class Car:
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class Toyotacar(Car):                            # here we use inheritance
#     def __init__(self,name):
#         self.name=name
# car1=Toyotacar("fortuner")
# car2=Toyotacar("prium")
# print(car1.start())
        
##single inheritance-1 parent 1 child
##multi-level inhertance-multiple classes
##multiple inheritance-
# class A:
#     varA="welcome to class A"
# class B:
#     varB="welcome to class B"
# class C(A,B):
#     varC="welcome to class C"
#     c1=C()

#     print(c1.varC)
#     print(c1.varB)
#     print(c1.varA)

#super class
# class Car:
#      def __init__(self,type):
#          self.type=type         
#      @staticmethod
#      def start():
#          print("car started")
#      @staticmethod
#      def stop():
#          print("car stopped")
# class Toyotacar(Car):                            
#      def __init__(self,name,type):
#          super().__init__(type)
#          self.name=name
#          super().start()
# car1=Toyotacar("fortuner","petrol")
# print(car1.type)
# print(car1.name)

# #class method
# # class Person:
# #     name="anonymous"
# #     def changename(self,name):
# #         self.__class__.name="rahul"       #this change the name from anon to rahul
# # p1=Person()
# # p1.changename("rahul")
# # print(p1.name)        # creaets a new name ie rahul
# # print(Person.name)

# class Person:
#     name="anonymous"
#     @classmethod
#     def changename(cls,name):
#         cls.name=name
# p1=Person()
# p1.changename("rahul")
# print(p1.name)
# print(Person.name)

# ##property decorator##
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     @property                         #this will create this formula into property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"
# stu1=Student(98,97,99)
# print(stu1.percentage)
# stu1.phy=86
# print(stu1.percentage)    
    
#polymorphism:operator overloading - same symbol different work +
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def shownumber(self):
#         print(self.real,"i +",self.img,"j")
#     def __add__(self,num2):     #dunder
#         newReal=self.real + num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)
# num1=Complex(1,3)
# num1.shownumber()

# num2=Complex(4,6)
# num2.shownumber()

# # num3 = num1.add(num2) 
# # num3.shownumber()       
# num3=num1+num2       #this happens because of dunder functions above ^
# num3.shownumber()  

#lets practice
# class Circle:    #1
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14*self.radius
# c1=Circle(21)
# print(c1.area())
# print(c1.perimeter())

# class Employee:   #2
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
#     def showdetails(self):
#         print("role =", self.role)
#         print("dept =",self.dept)
#         print("salary =",self.salary)
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#         super().__init__("engineer", "IT", "60000")

# engg1=Engineer("Akshat",22)
# engg1.showdetails()
        


