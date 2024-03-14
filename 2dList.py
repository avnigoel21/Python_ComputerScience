def create_2d_list(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input("enter the element"))
            row.append(element)
        matrix.append(row)
    return matrix


matrix =  create_2d_list(3, 3)
#print(matrix)
print("The 2d list:")
for row in matrix:
    print(row)

print(matrix[1][1])

# rows = 3
# cols = 3
# 1 2 3
# 4 5 6
# 7 8 9
            


# a = 6
# a1 = [5, 3, 2 , 8, 9]
# a1.sort()
# print(a1)


# list = [5, 8, 9, 3]

# print(list)
# # append - adding to the last
# list.append(2)
# print(list)
