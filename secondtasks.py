import random
import string
import re

print('''Welcome to HNG Employee Registration Page
Please Enter the following details as prompted'''
+ "\n")


user_container = dict()
#This takes the user's input
while True:
    first_name = input('Enter Your First Name: ')
    if len(first_name) < 2:
        print('Name should not be less than 2 letters')
        first_name = input('Enter Your First Name: ')
    last_name = input('Enter Your Last Name: ')
    if len(last_name) < 2:
        print('Name should not be less than 2 letters')
        last_name = input('Enter Your Last Name: ')
    email = input('Enter Your Email: ')  # The code below validates the email
    while True:
        if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z", email, re.IGNORECASE):
            break
        else:
            print('Invalid Email. Please enter a valid Email. example: someone@domain.com')
            email = input('Enter Your Email: ')
    user_container = {'First Name': first_name, 'Last Name': last_name, 'Email': email}
    # This generates lower-cased random letters
    password = first_name[:2] + ''.join(random.choice(string.ascii_lowercase) for i in range(5)) + last_name[-2:]
    print(f"""Password: {password}
    Are You satisfied with the given password?""")
    choice = input('Yes or No? : ')
    if choice.upper() == "NO":
        print('Please create a password')
        password = input('New Password: ')
        while len(password) < 7:
            print('Password should be more than 7 letters long')
            password = input('New Password: ')
            break
        print('Registration Completed.' + "\n")
    else:
        print('Registration Completed.' + "\n")
    user_container[email]['password'] = password
    second_choice = input('Do you want to register another user? [Yes / No] : ' + "\n").upper()
    if second_choice == "YES":
        continue
    else:
        break
print(user_container)