# A Tuple is like a list, but it's immutable, that means, it cannot be changed.

my_tuple = ('a','b','c','d','e','f')

print(10 in my_tuple)
print('a' in my_tuple)

# A tuple is faster than a list, because it's immutable

# A example of usage of a tuple in real life,is a geographic coordinate.
# 
# Tuples only contains two methods
# They are:
# 
# Count()

print(my_tuple.count('a'))  

# Index

print(my_tuple.index('e'))