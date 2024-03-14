#indexing   0         1           2           3
fruits = ['apple', "grapes" , "watermelon", "mango"]  # list

# i = 0
# while i <= 3:
#     print(fruits[i])
#     i = i + 1

# for i in range(4):
#     print(fruits[i])



# for i in range(1, 4, 2):
#      print(fruits[i])

# if ():
# else:

# for i in range(10) :
#     print(i)
#     # if i == 5:
#     #     break
# else:
#     print("finshed for loop: this is inside else of for")


# for i in range(10) :
#     if i == 5:
#         continue  # skip
#     print(i)

# else:
#     print("finshed for loop: this is inside else of for")


# for i in range(10):
#     pass


# write a program to print multiplication table of a given number using for loop

# write a program to find whether a given number is prime or not

# A personal identification number (PIN) is four digits. E.g. 2345. 
# Write a function that allows the user to enter a PIN. The program outputs, “Hello” 
# if the user enters the PIN correctly.
# If the user makes three incorrect attempts the program outputs, “Locked out”.


def checkingPin(correctPin):
    attempts = 0
    while attempts < 3: 
        userInput = input("please enter your pin: ")
        if userInput == correctPin:
            print("hello")
            return
        else:
            print("Try again")
            attempts = attempts + 1
    print("Locked out")

correctPin = "2345"
checkingPin(correctPin)