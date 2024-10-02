# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
import random


#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

def calculateSum(num1, num2):
    correctAnswer = num1 + num2
    return correctAnswer

if __name__ == '__main__':
    # Selects two random numbers
    number1 = random.randint(1,1000)
    number2 = random.randint(1, 1000)

    # Calculates the correct answer
    rightAnswer = calculateSum(number1,number2)

    # Asks the user for the answer
    userAnswer = int(input(f'What is the sum of: {number1} and {number2}? '))

    # Output after the user has put in a number
    if userAnswer == rightAnswer:
        print("Congratulations!")
    else:
        print('Incorrect, the correct answer is', rightAnswer)



