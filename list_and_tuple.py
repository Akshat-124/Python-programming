# # marks1= 95
# # marks2=66
# # marks3=70

# ##list-mutable
# marks=[95,66,70]
# print(marks)
# print(type(marks))
# print(marks[0])
# #we can store multiple type of data in list
# student = ["akshat",21]
# print(student)
# #list is mutable
# student[0]="yaksha"
# print(student)
# #slicing in list
# mark = [66,45,63,78]
# print(mark[1:4])

# #methods of list
# list = [2,1,3]
# list.append(4)
# print(list)
# list.sort()         #default ascending order
# print(list)
# list.sort(reverse=True)   #decending order
# list.reverse()
# print(list)
# list.insert(1,5)
# print(list)
# list.remove(5)
# print(list)
# list.pop(1)
# print(list)

#tuples-immutable
# tup = (2,1,3,1)
# print(tup[0])
# print(type(tup)) 
#tuple methods
# tup=(1,2,3,4)
# print(tup.index(2))

#lets practice-
# mov1=input("enter 1st movie: ")
# mov2=input("enter 2nd movie: ")
# mov3=input("enter 3rd movie: ")
# movies=[mov1,mov2,mov3]
# print(movies)

list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not a palindrome")
    




