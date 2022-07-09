# This is a program that calculates your age, based on the year informed

from datetime import date

current_year = date.today().year

date_birth = input('What year were you born?')
print(date_birth)
age = int(date_birth) 
age -= current_year
age *= -1
print(f'You are {age} years old!')