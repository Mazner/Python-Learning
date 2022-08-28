# Conditionals works like that on python:

enjoying_music = True
able_to_study = True

if enjoying_music:
    able_to_study = False
    print('You not are able to study, so you\'re enjoying the music')
else:
    able_to_study = True
    print('You are able to study, so you\'re not enjoying the music')

number_one = 52
number_two = 87
number_three = 43

if number_one > number_two:
    print('Number one is bigger than number two')
elif number_one > number_three:
    print('Number one is not bigger than number two, but it\'s bigger than number three')
