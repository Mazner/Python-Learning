def checkDriverAge(age):
    if age < 18:
        print(f'Sorry, you are {age} years old\nYou can\'t drive this car!')
    elif age == 18:
        print(f'Wow, just turned {age} right?\nGo on and drive')
    elif age > 18:
        print(f'Enjoy the ride!')
    else:
        print('Please, tell me a valid age')


checkDriverAge(18)