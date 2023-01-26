username = input('choose a username: ')
password = input('choose a password: ')
password_len = len(password)
hidden_password = '*' * password_len
print(f'Hey {username} your password {hidden_password} is {password_len} letters long')