# In Python we can use a declaration to set various arguments
# Follow the example:

def someFunction(*args): 
    '''
    This function will print the sum 
    of the numbers that the user will input
    '''
    return sum(args) 

print(someFunction(1,2,3,4,5))

# We can also use kwargs:

def someFunction2(**kwargs):
    '''
    this function will print the sum 
    of the numbers that the user will input
    '''
    total = 0
    for items in kwargs.values():
        total += items
    return total

print(someFunction2(num1 = 5, num2 = 6))

# Using both args and kwargs:

def someFunction3(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    total += sum(args)

    return total

print(someFunction3(1,2,3,4,5, num1 = 5 , num2 = 5))