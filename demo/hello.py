# 2 types of files:
# 1) Text file 
# 2) Binary files

# #  Use open function to read the content of a file!
# # f = open('hi.txt', 'r')
# f = open('hi.txt') # by dafault the mode is r (reading)
# # data = f.read() 
# # data = f.read(5) # reads first 5 characters from the file

# data1 = f.readline()
# data2 = f.readline()
# data3 = f.readline()
# data4 = f.readline()

# print(data1)
# print(data2)
# print(data3)
# print(data4)
# f.close()




# f = open('hi.txt' , 'w')
# f.write('Please write this to the file ')
# f.close()


# append mode - adding to the last
# f = open('hi.txt' , 'a')
# f.write('I am appending ')
# f.close()

# write a program to read the text from a given file "poems.txt" and 
# find out whether it contains the word twinkle

f = open('poems.txt', 'r')

text = f.read()


if 'twinkle' in text:
    print("yes present")
else:
    print("not present")



# list1 = ["apple" , "mango" , "banana"]

# str1 = "congratulations"

