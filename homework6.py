import random

def get_even_numbers(lower, upper):
    #rtype : lst
    return [num for num in range(lower, upper + 1) if num % 2 == 0]

def first_and_last(lst):
    #rtype : lst
    return [lst[0], lst[-1]]

def main():
    #part 1
    while True:
        lower = int(input("Enter the lower limit: "))
        upper = int(input("Enter the upper limit: "))
        if upper >= lower:
            break
        print("Upper limit must be greater than or equal to lower limit.")
    
    even_numbers = get_even_numbers(lower, upper)
    print(f"Even numbers between {lower} and {upper}: {even_numbers}")
    
    #part 2
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in feet: "))
    
    personal_info = []
    personal_info.append(name)
    personal_info.append(age)
    personal_info.append(height)
    print(f"Personal info: {personal_info}")
    
    #part 3
    numbers = []
    for i in range(4):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    print(f"Min number: {min(numbers)}")
    print(f"Max number: {max(numbers)}")
    
    numbers.sort()
    print(f"Sorted list: {numbers}")
    print(f"First element in sorted list: {numbers[0]}")
    print(f"Last element in sorted list: {numbers[-1]}")
    
    # 3b
    new_num = int(input("Enter one more number: "))
    numbers[2] = new_num
    print(f"Updated list: {numbers}")
    
    # 3c
    contains_five = 5 in numbers
    print(contains_five)
    
    # 3d
    string_numbers = [str(num) for num in numbers]
    print(f"List of numbers as strings: {string_numbers}")
    
    # 3e
    concatenated_list = numbers + string_numbers
    print(f"Concatenated list: {concatenated_list}")
    
    # Part 4
    random_numbers = [random.randint(0, 100) for _ in range(5)]
    print(f"Random numbers: {random_numbers}")
    
    random_numbers.reverse()
    print(f"Reversed random numbers: {random_numbers}")
    
    # 4b
    first_last = first_and_last(random_numbers)
    print(f"First and last elements: {first_last}")
    
    # 4c
    first_last_tuple = tuple(first_last)
    print(f"First and last as tuple: {first_last_tuple}")
    
    # part 5
    rows, cols = 3, 5
    grid = [[(r, c) for c in range(cols)] for r in range(rows)]
    print("2D List:")
    for row in grid:
        print(row)
    
    # extra credit
    random_numbers = [random.randint(0, 100) for _ in range(8)]
    new_list = [num / 2 if num > 50 else num for num in random_numbers]
    
    print(f"Original list: {random_numbers}")
    print(f"New list: {new_list}")

# Run the main function
if __name__ == "__main__":
    main()
