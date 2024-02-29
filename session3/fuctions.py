# built-in functions - already present in python
# user defined functions


# import os 
# def greet(name):
#     print("Good Day, " + name)

# greet("Arnav")

# path = "C:\\Users\\admin\\Desktop\\pythonSessions_arnav\\codes"

# print(os.chdir(path))


# def sum(num1, num2):
#     #print(num1 + num2)
#     return num1 + num2


# s = sum(2, 3)
# print(s)



# def greet(name = "user"):
#     print("Good Day, " + name)

# greet("Arnav")
# greet()

# write a program using function to find greatest of three numbers


# def user():
#     user1 = int(input("enter number"))
#     user2 = int(input("enter number"))
#     user3 = int(input("enter number"))

#     return user1,user2,user3
# def process(user1,user2,user3):
#     if user1 > user2:
#         if user1>user3:
#             return user1
#         else: 
#             return user3

#     else:
#         if user2 > user3:
#             return user2
#         else:
#             return user3
        

# max = process(98, 67, 45)
# print(max)

# def display(user1,user2,user3):
#     print(user1,user2,user3)


# searching techniques
# 1) linear search
# 2) binary search


# 1) linear search
# l1 = [20, 80, 40, 50, 10]

# element = 500

# def search(l1, element):
#     for i in range(len(l1)):
#         if l1[i] == element :
#             return i
#     else:
#         return -1

# result = search(l1, element)
# print(result)


# 2) binary search

# 1 step -> sort the array

l1 = [20, 80, 40, 50, 10]
element = 50

sorted_l1 = [10, 20, 40, 50, 80]

# 2 step -> find the mid of your list i.e 40 in this case

# 3 step -> compare mid point with your element (as 50 > 40 you need to see only right hand side of the list)

# 4 step -> again repeat the 2nd step to find the mid of second half

def binarySearch(sorted_l1, element, start, end):
    while(start <= end):
        #mid = (start + end) / 2
        mid = start + (end - start)//2
        
        if (sorted_l1[mid] == element):
            return mid
        elif (sorted_l1[mid] < element):
            start = mid + 1
        else:
            end = mid - 1
    return -1

result = binarySearch(sorted_l1, element, 0, 4)
print(result)

    





