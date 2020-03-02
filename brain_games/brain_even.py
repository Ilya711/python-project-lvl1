import prompt
import random
from brain_games.cli import welcome_user
from brain_games import welcome

print(welcome())

print(welcome_user())

def rule():
    print('Answer "yes" if number even otherwise answer "no".')

name = name()

def wrong_answer1():
    return print("'no' is wrong answer ;(. Correct answer was 'yes'.\n Let\'s try again, {name}!")

def wrong_answer2():
    return print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let\'s try again, {name}!")

def correct():
    print('Correct')

def wrong_input():
    print("Correct answer only 'yes' or 'no'")

def random_number():
    r_number = random.randint(1, 100)
    return r_number

def main():
    count = 0
    correct_answer = 0
    while count <= 0:
        numb = random_number()
        print('Question: ' + str(numb))
        answer = prompt.string('Your answer: ' )
        if numb % 2 == 0 and answer == 'yes':
            correct()
            count += 1
            correct_answer += 1
        elif numb % 2 == 1 and answer == 'no':
            correct()
            count += 1
            correct_answer += 1
        elif numb % 2 == 0 and answer == 'no':
            wrong_answer1()
            count += 3 #завершает игру
        elif numb % 2 == 1 and answer == 'yes':
            wrong_answer2()
            count += 3 #завершает игру
        else:
            wrong_input()
        if correct_answer == 3:
            print("Congratulations, {name}")

if __name__ == "__main__":
    main()



