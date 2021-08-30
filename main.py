# import nested
# import histogram
# import heading_generator
# import guessing_game
# import login
# import greeting_arguments
# import fizzbuzz
# import web_scraper
# import scraper_using_bs4
# import secret_secrets

print("What program would you like to run?")
print('Guessing Game? Y or N')
answer = input()
if answer.upper() == 'Y':
  import guessing_game
else:
  print('To-do List? Y or N')
  answer = input()
  if answer.upper() == 'Y':
    import greeting_arguments
  else: 
    print('FizzBuzz? Y or N')
    answer = input()
    if answer.upper() == 'Y':
      import fizzbuzz
    else:
      print('Would you like to order waffles? Y or N')
      answer = input()
      if answer.upper() == 'Y':
        import secret_secrets
      else:
        print('Awww...ok. Come play when you aren\'t busy, ok?')