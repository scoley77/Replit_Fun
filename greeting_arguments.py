#good morning, sara coley, here is what we need to do today: or ...here is what needs to be done tomorrow
user = {
  'first' : 'Sara',
  'last' : 'Coley'
}

def greeting():
  to_dos = tuple()

  def commence(day, *args, **kwargs):
    print(f"\nGood {day}, {kwargs['first']} {kwargs['last']}. {task_intro}")
    for arg in args:
      print(arg)

  print("What time of day is it?")
  daytime = input().lower()

  if daytime == 'morning' or daytime == 'noon' or daytime == 'afternoon':
    task_intro = 'Here is what needs to be done today:'
  elif daytime == 'evening' or daytime == 'night':
    task_intro = 'Here is what needs to get done tomorrow:'
  else:
    task_intro = 'Here is your to-do list:'

  print('To-do list:')
  while True:
    item = input()
    if item == 'done':
      commence(daytime, *to_dos, **user)
      return False
    else:
      to_dos += (item,)
      continue
greeting()

  