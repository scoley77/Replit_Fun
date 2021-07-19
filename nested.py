cousins = {
  'gardners' : ['Xander', 'Callan'],
  'coleys' : ['Jay', 'Wiley'],
  'andersons' : ['Tannon', 'Barrett', 'Graham', 'Ava'],
  'our family' : ['Juniper', 'Winry', 'Kylan']
}

def first_born(dict):
  list = []
  for key in dict.values():
    list.append(key[0])
  return list
  
print(f'Oldest children: ' + str(first_born(cousins)))

def youngest(dict):
  list = []
  for key in dict.values():
    list.append(key[-1])
  return list

print(f'Youngest children: ' + str(youngest(cousins)))