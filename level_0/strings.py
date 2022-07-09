# How strings work

# there's a declaration for a long string, we use 3 single quotes in a row: '''

from datetime import datetime

long_string = '''
Hey,
you see... I can be a string with a
lot of characters and also, you can

f <-
o <-
r <-
m <-
a <-
t <-

me the way you want

'''
print(long_string)

# We can also concatenate string using the '+' operator, example:

first_name = 'Marcos'
last_name = 'Rampaso'
full_name = first_name + ' ' + last_name

print(full_name)

# How we transform a integer into a string?
# for that we can use the 'type(thing)', for
# example: ###

number_integer = 132  # <- this is a int

string_formated = 'this is a integer ->' + str(number_integer) + '''
but it was transformed to a string for it to be printed here'''

print(string_formated)

# We can also use the escape sequence for printing single quotes, double quotes, etecetera

print("\n")
today = datetime.now()
print("today is the year of " + today.strftime("%Y") + '''
Of the ''' + today.strftime("%B") + ' month''\nAnd is a beautiful ' + today.strftime("%A"))

# Let's format the last string, so it can be more developer friendly

name = 'Marcos'
print(f'\nHi {name}!\nToday is {today.strftime("%A")}.\nWell, have a nice day!')

# Strings are indexed like arrays, so:

string_is_array = 'ABCDEFGHIJ'

# string  012345678
# Also, that array can be manipulated by
# string_is_array[start:end:stepover]

print('\n'+string_is_array[0:5:2])  # = ACE
# 0 = A
# 2 = C
# 3 = E
# In python, the negative of a index = the end,
# so, -1 = j
# Lets show and example by doing reversing an order

string_is_array = '012345678'
print('\n' + string_is_array[::-1])

# We can also get the length of a string using the 'len' function
print('\nThe length of the last array is:')
print(len(string_is_array))

# Note that the len count like humans, so the lenght is 9, but in computer
# Language, it's 0-8

# Another cool thing to do is:

print(string_is_array[0:len(string_is_array)])