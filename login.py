username = 'sarrrr'
email = 'sar@email.com'
password = 'jootube'

def login():
  print('email/username?')
  cred = input()
  print('password?')
  word = input()
  if cred == username and word == password or cred == email and word == password:
    print(f'hi, {username}')
  else:
    print('who are you?')

login()
    
