def calculate_factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= i+1
    return factorial

def series_sum(start, end, inc):
    sum = 0
    for i in range(start, end+1, inc):
        sum += i
    return sum

def find_min(a, b):
    if a < b:
        return a
    else:
        return b
    
def calculate_average(scores):
    sum = 0
    for i in scores:
        sum += i
    return round(sum/len(scores), 2)

def determine_grade(grade):
    if(grade >= 90):
        print("Congrats, you got an A!")
    elif(grade >= 80):
        print("Well done, you got a B!")
    elif(grade >= 70):
        print("You got a C!")
    elif(grade >= 60):
        print("You got a D. Better luck next time.")
    else:
        print("You recieved an F. Booooooooooo.")

def falling_distance(falling_time):
    return(.5*(9.8)*(falling_time**2))

def main():
    num = int(input("Enter the value you'd like to calculate the factorial for: "))
    print(f"Factorial of {num} is {calculate_factorial(num)}\n")

    start = int(input("Enter the starting value of the series: "))
    end = int(input("Enter the ending value of the series: "))
    inc = int(input("Enter the increment value of the series: "))
    print(f"The sum of the series {start} through {end} is = {series_sum(start, end, inc)}, with an increment of {inc}\n")

    print("Lets find the min of two values!")
    num1 = int(input("Enter the first value youd like to compare: "))
    num2 = int(input("Enter the second value youd like to compare: "))
    print(f"The minimum of {num1} and {num2} is {find_min(num1, num2)}\n")

    #i know the problem asked for specifically four, but this provides more functionality
    #did we learn about lists yet?? i forget, pls dont take off points
    test_scores = []
    score = ""
    print("\t !Enter done to finish inputting scores!")
    while score != "done":
        score = input("Enter the values of your test scores one at a time: ")
        if(score.isdigit() and float(score) >= 0):
            score = float(score)
            test_scores.append(score)
            continue
        if(score != "done"):
            print("\nPlease enter a non-negative number or done.\n")
    print(f"The average of your test scores is {calculate_average(test_scores)}")
    determine_grade(calculate_average(test_scores))
    print()

    for t in range(1,11):
        print(f"The distance an object has fell over an interval t={t} seconds is {round(falling_distance(t),2)} meters")

if __name__ == "__main__":
    main()