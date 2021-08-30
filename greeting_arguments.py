#order of *args and **kwargs is very important!!
def greeting():
  to_dos = tuple()
  user = {
  'first' : name,
  'honorific' : 'sama'
  }

  def commence(day, *args, **kwargs):
    print(f"\nGood {day}, {kwargs['first']}-{kwargs['honorific']}. {task_intro}")
    for arg in args:
      print(arg)

  if daytime.lower() == 'morning' or daytime.lower() == 'noon' or daytime.lower() == 'afternoon':
    task_intro = 'Here is what needs to be done today:'
  elif daytime.lower() == 'evening' or daytime.lower() == 'night':
    task_intro = 'Here is what needs to get done tomorrow:'
  else:
    task_intro = 'Here is your to-do list:'

  print('To-do list: (type \'done\' when finished)')
  while True:
    item = input()
    if item == 'done':
      commence(daytime, *to_dos, **user)
      return False
    else:
      to_dos += (item,)
      continue

print('Name?')
name = input()
print("What time of day is it?")
daytime = input()
greeting()

  