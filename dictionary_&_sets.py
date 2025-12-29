# dictionary 
# info = {
#     "key":"value",
#     "name":"akshat",
#     "learning":"coding",
#     "age":21,
#     "subjects":["python","java","c"],
#     12.99:11
# }
# print(info)
# print(info["name"])   #individual values also print
# info["name"]="yaksha"
# info["surname"]="dwivedi"
# print(info)
#dict are unordered no index , mutable , we cant create duplicate keys

# #nested dict
# student = {
#     "name":"akshat",
#     "sub" : {
#         "phy":88,        #nested dict
#         "chem":90
#     }
# }
# print(student)
# print(student["sub"]["phy"])

#methods dict
# student = {
#     "name":"akshat",
#     "sub" : {
#         "phy":88,        #nested dict
#         "chem":90
#     }
# }
# print(student.keys())
# print(len(list(student.keys())))       #we can store one data type into another i.e dict to list list to dict
# print(student.values())
# print(list(student.items()))
# student.update({"city":"delhi"})
# print(student)


## sets
#collection of unordered items. each collection is unique and immutable
#we cannot store list and dict in sets cuz they are mutable
# collection = {1,2,3,4,"hello","world","world"}
# print(collection)
# print(type(collection))
# print(len(collection))

# collection = set() #empty set
# print(collection)

# sets-mutable but set-elements-immutable

#sets methods
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.remove(2)
# print(collection)
# collection.add("AKD")
# print(collection)
# collection.clear()
# print(len(collection))
# collection = {"hello","world","AKD"}
# print(collection.pop())     #random elements pops
# print(collection.pop())

#imp set methods
#set.union(set2)
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.union(set2))
# print(set1)
# print(set2)
# #set intersection
# print(set1.intersection(set2))

#lets practice
#1
# ques1 = {
#     "table":["a piece of furniture","list of facts and figure"],
#     "cat":"a small animal"
# }
# print(ques1)

#2
# classroom = {
#     "python","java","c++","python","javascript","java","c++","c"
# }
# print(classroom)
# print(len(classroom))

#3
# sub1 = int(input("enter the marks in sub1: "))
# sub2 = int(input("enter the marks in sub2: "))
# sub3 = int(input("enter the marks in sub3: "))
# marks = {
#     "subject1":sub1,"subject2":sub2
# }
# print(marks)

# marks = {}
# x = int(input("enter phy: "))
# marks.update({"phy":x})
# y = int(input("enter chem: "))
# marks.update({"chem":y})
# print(marks)

#4
# values = {9,9.0,9.35,"9.0"}
# print(values)

# values = {
#     ("float",9.0),
#     ("int",9)
# }
# print(values)