# In class assignment 6 (aka Lab 6)
# Names: Ben Zakielarz
def main():
    my_list = ['A', 'B', 'C', 'D', 'E']

    # Question 1, loop through each element in my_list and print each element separated by a comma
    for index, item in enumerate(my_list):
        if index == len(my_list) - 1:
            print(item)
        else:
            print(item, end=", ")
    print()

    # Question 2, loop through my_list by index and print each element separated by a comma
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            print(i)
        else:
            print(i, end=", ")
    print()

    # Question 3, print only the first element in my_list
    print(my_list[0])
    print()
    # Question 4, print the last element of the list in 2 different ways
    # Do not hardcode the number 5 anywhere for this problem
    print(my_list[len(my_list)-1])
    print(my_list[-1])
    print()
    # Question 5, ask the user to input a letter then print true if that letter is in my_list otherwise print false
    # 1 bonus point if you can do this in 1 line of code (without using the keyword if)
    print(input("Enter a letter: ") in my_list)
    print()
    # Question 6, ask the user to enter a decimal, and an integer index (0,5)
    # then insert the decimal into my_list at the given index
    # then print the list
    decimal = float(input("Enter a decimal: "))
    index = int(input("Enter an ineex 0-5: "))
    my_list.insert(index, decimal)
    print(my_list)
    print()
    # Question 7, complete function find_num_in_range, so it returns the first item in the list that is
    # between [lower_limit, upper_limit], if no number is in the range return None
    # Get user input for the lower and upper limit
    def find_num_in_range(num_list, lower_limit, upper_limit):
        for i in num_list:
            if i >= lower_limit and i <= upper_limit:
                return i
        return "None"

    num_list = [66, 71, 2, 34, 99, 17, 30, 55]
    num_list.sort()

    lower_lim = int(input("Enter lower limit: "))
    upper_lim = int(input("Enter upper limit: "))
    print(find_num_in_range(num_list, lower_lim, upper_lim))
    print()

# no changes below this comment
if __name__ == '__main__':
    main()
