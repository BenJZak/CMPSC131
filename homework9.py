import random

def main():
    print("------------------------------------------------------------------------")
    l1 = [random.randint(1, 100) for _ in range(10)]
    print(f"Initial list 1: {l1}")
    print(f"Bubble Sort list 1: {bubble_sort(l1)}")
    print(f"First, Middle, Last, of list 1: {first_middle_last(l1)}")
    print("------------------------------------------------------------------------")
    l2 = [random.randint(101, 200) for _ in range(10)]
    print(f"Initial list 2: {l2}")
    print(f"Selection Sort list 2: {selection_sort(l2)}")
    print(f"First, Middle, Last, of list 2: {first_middle_last(l2)}")
    print("------------------------------------------------------------------------")

def bubble_sort(lst):  #https://en.wikipedia.org/wiki/Bubble_sort#Implementation
    sorted_lst = lst.copy()  # Copy to avoid changing the original list
    swapped = True
    while swapped:  # Continue until no swaps are needed
        swapped = False
        for i in range(1, len(sorted_lst)):
            if sorted_lst[i-1] > sorted_lst[i]:  # Swap if the previous item is larger
                temp = sorted_lst[i]
                sorted_lst[i] = sorted_lst[i-1]
                sorted_lst[i-1] = temp
                swapped = True
    return sorted_lst

def selection_sort(lst):  #https://en.wikipedia.org/wiki/Selection_sort#Implementations
    sorted_lst = lst.copy()  # Copy to avoid changing the original list
    for i in range(len(sorted_lst) - 1):
        min_element = i
        for j in range(i + 1, len(sorted_lst)):
            if sorted_lst[j] < sorted_lst[min_element]:  # Find the smallest element
                min_element = j
        if min_element != i:  # Swap the found minimum with the current position
            temp = sorted_lst[i]
            sorted_lst[i] = sorted_lst[min_element]
            sorted_lst[min_element] = temp
    return sorted_lst

def first_middle_last(lst):  # Get the first, middle, and last elements
    first = lst[0]
    last = lst[-1]
    middle = lst[len(lst) // 2]
    return first, middle, last

if __name__ == "__main__":
    main()
