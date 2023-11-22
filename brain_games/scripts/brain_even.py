#!/usr/bin/env python3

from random import randint
import prompt


ran = 0
count = 0
print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print("Hello, " + str(name) + "!")
print('Answer "yes" if the number is even, otherwise answer "no".')
while count < 3:
  ran = randint(1, 100)
  answer = prompt.string('Question: '+ str(ran) + '\nYour answer: ')
  if (answer == 'yes' and int(ran) % 2 == 0) or (answer == 'no' and int(ran) % 2 != 0):
      print('Correct!')
      count += 1
  else:
      print("'yes' is wrong answer ;(. Correct answer was 'no'.'\nLet's try again, " + str(name) + "!")
      break
if count == 3:
  print("Congratulations, " + str(name) + "!")

if __name__ == '__main__':
    main()
