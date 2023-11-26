#!/usr/bin/env python3


import random
import prompt

def generate_random_values():
    return random.randint(1, 50), random.randint(1, 10), random.choice(
        ['+', '-', '*'])

def calculate_correct_result(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2

def welcome():
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name? ')
  print(f"Hello, {name}!")
  return name

def play_round(num1, num2, operator):
    correct_result = calculate_correct_result(num1, num2, operator)
    print(f"Question: {num1} {operator} {num2}")
    user_response = int(input('Your answer: '))

    if user_response == correct_result:
        print("Correct!")
        return True
    else:
        print(f"{user_response} is the wrong answer ;(. Correct answer was {correct_result}.")
        return False

def play_game(name, rounds=3):
    correct_count = 0

    for _ in range(rounds):
        num1, num2, operator = generate_random_values()
        if play_round(num1, num2, operator):
            correct_count += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if correct_count == rounds:
        print(f"Congratulations, {name}!")
