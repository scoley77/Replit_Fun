# fizz for 3x, buzz for 5x, fizzbuzz for both

fizz_range = range(1, 101)

def fizzbuzz(num_list):
  for num in num_list:
    if num % 15 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)

fizzbuzz(fizz_range)