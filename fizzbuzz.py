# fizz for 3x, buzz for 5x, fizzbuzz for both

def fizzbuzz(max_num):
  for num in range(1, 1 + max_num):
    if num % 5 == 0 and num % 3 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)

print('Max number:')
while True:
  answer = float(input())
  if type(answer) == int or float:
    fizzbuzz(int(answer))
    False
  else:
    print('Try entering a number...') 
