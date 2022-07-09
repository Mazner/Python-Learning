# This is a program that calculates your age, based on the year informed

from datetime import date

current_year = date.today().year

date_birth = input('What year were you born?')
# The next operation is not a optimal answer (it was my first), but it'll work

age = int(date_birth) #age receives the integer of the date of birth
age -= current_year   #age - our current year = negative actual age
age *= -1             #So we just multiply it by -1

print(f'You are {age} years old!')