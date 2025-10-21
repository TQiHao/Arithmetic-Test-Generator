#provides function for generating random numbers and performing random operations 
import random

# Generate and return 2 single digits function.

def generate_single_number():
    # random integer between 0 to 9 
    return random.randint(0, 9), random.randint(0, 9)

# Generate and return the operators (+, -, *)

def generate_operator():
    # choose a random choice from the list
    return random.choice(["+", "-", "*"])

# come out with 3 different types of equation with 3 different operators

def question(a, b, operator):
    print(f"{a} {operator} {b} = ?")

def results_of_question(a, b, operator):
    if operator == "+": 
        return a + b
    elif operator == "-":
        return a - b 
    elif operator == "*":
        return a * b 
    
# come out with a message telling users his/her result in percentage
    
def print_result_message(score, total):
    percentage = (score / total) * 100
    print(f"your score: {score} / {total}")
    print(f"Marks = {percentage:.1f}%")

    if percentage < 50:
        print("You have failed the test")

    elif percentage < 80: 
        print("You passed the test, please improve it")

    elif percentage < 100:
        print("Well done, keep it out")

    else:
        print("excellent")

# Generate at least 5 and max 10 questions
# Number of question in the range of 5 to 10

def arithmetric_test():
    number_of_questions = random.randint(5, 10)
    print("Welcome to arithmetric test\n")
    print(f"You have to do {number_of_questions} questions")
    print("Good luck\n")

    # initialization
    # ensure the score starts from 0 then slowly go up

    score = 0 

    #e.g in the range of 7, 
    # i = 0
        # 1
        # 2 
        # 3 
        # 4
        # 5 
        # 6 
        # 7 

    for i in range(number_of_questions):
        a, b = generate_single_number()
        operator = generate_operator()

        # i start from 0, therefore i = 0, i + 1 = 1 

        print(f"Question {i + 1}: ", end="")
        question(a, b, operator)

        user_answer = int(input("Your answer: "))
        correct_answer = results_of_question (a, b, operator)

        if user_answer == correct_answer:
            print("Ok\n")
            score += 1

        else:
            print("Wrong\n")

    print_result_message(score, number_of_questions)   

arithmetric_test()     

input("Press enter to terminate")



