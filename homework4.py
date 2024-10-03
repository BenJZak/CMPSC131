# Complete the functions so that this program works exactly the same as classAverages.py

# This function must return something for the while loop to use
def is_score_valid(score):
    if(score >= 0 and score <= 100):
        return False
    return True


# This function should not return anything
def calculate_and_print_class_average(total, number):
    class_average = total / number
    print(f'Class average is {class_average}')


# We want a program that lets a user enter the name of a class,
#  a number of students and the number of exams.
#  Then we want to collect the grades for each exam and output the average grade per student.
#  We also want to output the average of all exams for the whole class.
#  We should ask the user if they want to repeat the process for another class
#  Let's validate that the grades entered are between [0, 100]

gradesLoop = True

while gradesLoop:
    # collect the input
    className = input('\nEnter the class name: ')
    numberOfStudents = int(input("Enter number of students: "))
    numberOfExams = int(input("Enter number of exams: "))
    classTotal = 0
    # loop though the number of students
    for s in range(0, numberOfStudents, 1):
        studentTotal = 0
        print(f"\nStudent {s + 1}'s info")
        # loop though the number of exams
        for n in range(numberOfExams):
            score = float(input("Enter score for exam " + str(n + 1) + ": "))
            # validate the score
            # TODO: pass an argument into is_score_valid
            while is_score_valid(score):
                print(score, f'is out of range')
                score = float(input(f"Enter score for exam {n + 1}: "))
            studentTotal += score
        # When we are done collecting the scores for a student, calculate their average
        studentAverage = studentTotal / numberOfExams
        classTotal += studentAverage
        print('Student ' + str(s + 1) + "'s average is " + str(studentAverage) + '\n')
    # TODO: pass arguments into calculate_and_print_class_average
    calculate_and_print_class_average(classTotal, numberOfStudents)

    anotherClass = input("Do you have another class? y/n ")
    if anotherClass == 'n':
        gradesLoop = False

