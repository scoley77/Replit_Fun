import random

def guessing_game():
  answer = random.randint(0, 100)
  while True:
    print('What is your guess?')
    guess = int(input())

    if guess == answer:
      print('yay! you did it!')
      print('play again? Y or N')
      response = input()
      if response == 'Y':
        guessing_game()
      else:
        print('ok.')
        return False
    elif guess < answer:
      print('too low!')
    elif guess > answer:
      print('too high!')
  
guessing_game()