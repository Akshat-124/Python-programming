## while loops
# while conditions :
#####some work
# count=1 #iterators-i,j,k,count
# while count<=5: #iteration
#     print("hello",count)
#     count+=1
#lets practice
#1.print no. from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1
#2.print no. from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1
#3.print multiplication table of a number n
# def mul(n):
#     i=1
#     while i<=10:
#         print(n*i)
#         i+=1
# n=3
# print(mul(n))
#4. print elements of list using loop
# def elements(nums):
#     n=len(nums)
#     i=0
#     while i<n:
#         print(nums[i])
#         i+=1
# nums=[1,4,9,16,25,36,49,64,81,100]
# print(elements(nums))
#5. search for no. x in tuple
# def search_element(nums,x):
#     n=len(nums)
#     i=0
#     while i<n:
#         if nums[i]!=x:
#             i+=1
#         else:
#             return x,i
#     return False
# nums=[1,4,9,16,25,36,49,64,81,100]
# print(search_element(nums,81))    

# break - lops terminates 
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
#continue - terminates current iteration
# i=1
# while i<=5:
#     if(i==3):
#         i+=1
#         continue #skip
#     print(i)
#     i+=1

#FOR loops
#seq traversal list,string,tuples,etc.
# veggies = ["potato","brinjal"]
# for val in veggies:
#     print(val )
#1.print the elements of following list using a for
# def elements(nums):
#     n=len(nums)
#     for i in range(0,n):
#         print(nums[i])
#         i+=1
# nums=[1,4,9,16,25,36,49,64,81,100]
# print(elements(nums))    
#2.search no x in tuple
# def search(nums,x):
#     n=len(nums)
#     for i in range (0,n):
#         if nums[i]==x:
#             return x,i
#     return False
# nums=(1,4,9,16,25,36,49,64,81,100)
# print(search(nums,35))  
# 
# 
# lets practice
# #1.wap to find sum of first n numbers
# n=5
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("total sum=", sum)    
# #2.factorial of n number
# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("factorial=", fact)    

 
 

        
