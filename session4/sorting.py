# sorting techniques
# 1) Bubble sort
# 2) Selection sort
# 3) insertion sort 

def bubbleSort(l1):
    n = len(l1) # length of the list

    for i in range(n):
        for j in range(0, n-i-1):
            if(l1[j] > l1[j+1]):
                #swap
                l1[j] , l1[j+1] = l1[j+1], l1[j]


def selectionSort(l1):
    n = len(l1)

    for i in range(n):
        min_index = i
        for j in range(i+1 , n):
            if (l1[j] < l1[min_index]):
                min_index = j
        l1[i], l1[min_index] = l1[min_index] , l1[i]


l1= [7, 9, 1, 4]

print("original list is: ")
print(l1)

bubbleSort(l1)

print("sorted list with bubbleSort: ")
print(l1)

l2 = [7, 9, 1, 4]

selectionSort(l2)

print("sorted list with SelectionSort: ")
print(l2)

