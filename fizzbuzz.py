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

fizzbuzz(100)