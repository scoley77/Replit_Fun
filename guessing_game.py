import random

def guessing_game(max_num):
  answer = random.randint(0, max_num)
  while True:
    print('What is your guess?')
    guess = int(input())

    if guess == answer:
      print('yay! you did it!')
      print('play again? Y or N')
      response = input()
      if response.upper() == 'Y':
        guessing_game()
      else:
        print('ok.')
        return False
    elif guess < answer:
      print('too low!')
    elif guess > answer:
      print('too high!')

print('Max number:')
while True:
  answer = float(input())
  if type(answer) == int or float:
    guessing_game(int(answer))
    False
  else:
    print('Try entering a number...') 
