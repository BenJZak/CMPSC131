'''Write a python program that asks the user for a number in the range of 1 through 7. The
program should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3=
Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an error
message if the user enters a number that is outside the range of 1 through 7. Must use an else statement
for full credit.'''

user_input = input("Enter a number between 1 and 7: ")
while True:
    try:
        value = int(user_input)
        if 1 <= value <= 7:
            if(value == 1):
                print("Monday!")
                break
            if(value == 2):
                print("Tuesday!")
                break
            if(value == 3):
                print("Wednesday!")
                break
            if(value == 4):
                print("Thursday!")
                break
            if(value == 5):
                print("Friday!")
                break
            if(value == 6):
                print("Saturday!")
                break
            if(value == 7):
                print("Sunday!")
                break
        else:
            print("Error: The number must be between 1 and 7. Please try again.")
            user_input = input("Enter a number between 1 and 7: ")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        user_input = input("Enter a number between 1 and 7: ")


'''A software company sells a package that retails for $99. Quantity discounts are given
according to the following table: (No discount when less than 10 packages are bought)
Quantity Discount
10 - 19 10%
20 - 39 20%
40 - 79 30%
80 or more 40%
Write a program that asks the user to enter the number of packages purchased. The program should then
display the amount of the discount (if any) and the total amount of the purchase after the discount. You
must display the prices with a dollar sign and 2 decimal places'''

user_input = input("Enter the number of packages purchased: ")
while True:
    try:
        value = float(user_input)
        if(value < 10):
            print("Total: $", value*99)
            break
        elif(value < 20):
            print("Total: $", value*99)
            print("Discount:", round((value*99 - value*99*.9),2))
            print("Total after discount:", round((value*99*.9),2))
            break
        elif(value < 40):
            print("Total: $", value*99)
            print("Discount:", round((value*99 - value*99*.8),2))
            print("Total after discount:", round((value*99*.8),2))
            break
        elif(value < 80):
            print("Total: $", value*99)
            print("Discount:", round((value*99 - value*99*.7),2))
            print("Total after discount:", round((value*99*.7),2))
            break
        else:
            print("Total: $", value*99)
            print("Discount:", round((value*99 - value*99*.6),2))
            print("Total after discount:", round((value*99*.6),2))
            break
    except ValueError:
        user_input = input("Error: Enter a number: ")

'''Write a Python program that will calculate (and display) the total of the following5
series of numbers (using loop):
4 + 7 + 10 + 13 + ⋯ + 25 + 28'''
sum = 0
for i in range(4, 31, 3):
    print(i)
    sum += i
print(sum)

'''Write a Python program that reads a positive integer and outputs the number in
reverse order. You must convert the input to an integer and use a loop with the mod operator for
full credit. For example, the reverse of 123 is 321 and the reverse of 728 is 827.'''
reversed_num = 0
user_input = int(input("Enter a number you'd like reversed: "))
while user_input > 0:
    digit = user_input % 10  #get the last digit
    reversed_num = reversed_num * 10 + digit  #shift and add the digit
    user_input //= 10  #remove the last digit from user_input
print(reversed_num)

'''A prime number is an integer greater than 1 and divisible by only itself and 1. For
example, 2, 3, 5, 7, 11, 13 are prime numbers. Write a program that reads a positive integer then
outputs whether it is a prime number or not. [Hint: if n is a multiple of any numbers from 2 to n-1 then
n is NOT a prime number.] You must use a loop for full credit.'''

#This is so terrible and I hate this solution but it works idk, there HAS to be a prettier way to do this lol
user_input = int(input("Enter a vlue to check if it is a prime number: "))
if(user_input <= 3 and user_input > 1):
    print("Prime!")
elif(user_input == 1 or user_input == 0):
    print("Not Prime! (kinda)")
else:
    counter = 0
    for i in range(2, user_input):
        if (user_input % i == 0):
            counter += 1
    if(counter >= 1):
        print("Not Prime!")
    else:
        print("Prime!")



