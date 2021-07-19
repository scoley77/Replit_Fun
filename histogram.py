"""
Two ways to create this histogram
g $$$$$$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$
o $$$$$$$$$$$$$
"""

chart = {
  'g' : 22 * '$',
  'f' : 35 * '$',
  't' : 9 * '$',
  'o' : 12 * '$'
}

def histogram():
  for key, value in chart.items():
    print(f'{key} {value}')

histogram()

sales = {
  'google' : 22,
  'facebook' : 35,
  'twitter' : 9,
  'offline' : 12
}

def hist():
  for key, value in sales.items():
    print(key[0] + ' ' + value * '$')

hist()