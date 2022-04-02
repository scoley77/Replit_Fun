class Waffles:
  def __init__(self, customer, total):
    self.customer = customer
    self._total = total

  _toppings = ['blueberries', 'strawberries', 'banana', 'nutella', 'whipped cream']
  __secret_menu = ['yogurt', 'fruit loops', 'ham & swiss', 'chocolate chips']
  
  @property
  def total(self):
    return self._total

  @property
  def secret_menu(self):
    return self.__secret_menu

  def secret_order(num):
    return Waffles.__secret_menu[int(num - 1)]

  combos = ()

  def order(customer, *args):
    reqs = ()
    for arg in args:
      reqs += (Waffles._toppings[int(arg) - 1],)
    Waffles.total = 4.00 + len(reqs) * 0.75 
    
    print('Can I get you anything else?')
    key_ = input()
    if key_.strip().lower() == 'yes' or key_.strip().lower() == 'yes, please':
      print("Oh?")
      pass_ = input()
      if pass_.strip().lower() == 'cupcakes and sugar':
        print('As you wish; make your order. (1 - 4)')
        secret = float(input())
        Waffles.total += 1.50
        Waffles.total = '${:,.2f}'.format(Waffles.total * 1.06)
        print(f'{customer} ordered waffles with {", ".join(reqs)}, and {Waffles.secret_order(secret)}. The total is {Waffles.total}. Thank you for coming!')
      else:
        Waffles.total = '${:,.2f}'.format(Waffles.total * 1.06)
        print(f'{customer} ordered waffles with {", ".join(reqs)}. The total is {Waffles.total}. Thank you for coming!')
    else:
      Waffles.total = '${:,.2f}'.format(Waffles.total * 1.06)
      print(f'{customer} ordered waffles with {", ".join(reqs)}. The total is {Waffles.total}. Thank you for coming!')
    
print('Hi')
print('What would you like to order? Say \"that\'s it" when you\'re finished. (1 - 5)')
while True:
  tops = input()
  if tops == '1' or tops == '2' or tops == '3' or tops == '4' or tops == '5':
      Waffles.combos += (tops,)
  elif tops.lower() == 'that\'s it':
    break
    continue
  else:
    print('Looks like that isn\'t on our menu; try again.')
print('Could I get a name for the order?')
name = input()
Waffles.order(name, *Waffles.combos)