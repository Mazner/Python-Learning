# This will convert the password to ****
# and also, it'll show the password lenght


username = input('Hello, tell me your username\n>')
password = input('Now tell me your password\n>')

password_encrypted = '*' * len(password) #This is taking the '*' character the lenght of the password

print(f"Hey {username}, your password {password_encrypted} is {len(password)} digits long")