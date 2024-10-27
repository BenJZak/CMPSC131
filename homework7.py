import random
import math

'''Create a 2d list with 7 rows and a random number of columns between [1,10] in each
row. Fill the list with all zeros. Print the list. Loop through the list and print the number of
columns in each row.'''

matrix = [[0 for _ in range(random.randint(1,10))] for _ in range(7)]
print(matrix)
index = 1
for row in matrix:
    print(f"Columns in row {index}: {len(row)}")
    index += 1

'''Write a function for linear search and a function for binary search. Generate a list of 25
random integers between [1,100]. Print the list, then call both functions searching for the
number 13. Print the returned boolean from each search function'''
def linear_search(array):
    search_term = 13
    for i in array:
        if i == search_term:
            return True
    return False
def binary_search(array):
    array = sorted(array)
    search_term = 13
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = math.floor((left+right)/2) #source for binary_search algo: https://en.wikipedia.org/wiki/Binary_search#Algorithm
        if(array[middle] < search_term):
            left = middle + 1
        elif(array[middle] > search_term):
            right = middle - 1
        else:
            return True, "Index: " + str(middle)
    return False

intlist = [random.randint(1,100) for _ in range(25)]
print(intlist)
print(sorted(intlist))
print(f"Result of linear_search: {linear_search(intlist)}")
print(f"Result of binary_search: {binary_search(intlist)}")