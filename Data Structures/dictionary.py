#   A dictionary is a unordered key - value pair
#   What does that mean? It means that we can assign
#   a key to a value, like this:

my_dictionary = {
    'a' : 123,
    'b' : 'This is the letter B',
    'last' : 789
}

print(my_dictionary['a'])
print(my_dictionary['b'])
print(my_dictionary['last'])

# We can also do it using matrixes, follow the example

matrixed_dict = [
    {
    'a' : 'element of the first line',
    'b' : [2,3,4],
    'c' :789
    },
    {
    'a' : 'Element of the second line',
    'b' : 'Second column',
    'c' : 42.23
    }
]
print(f"\n\n")
print(matrixed_dict[0]['a'])
print(matrixed_dict[1]['c'])
print(matrixed_dict[0]['b'])

#   Dictionaries are unordered, but they can be useful in some things
#   for instance: a game character