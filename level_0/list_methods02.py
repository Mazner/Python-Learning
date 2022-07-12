#   Continuation of the list methods

#                   index                   #
#   It returns the index of the informed element (it's position)

array = [10,20,30,40,50,30]

print(f"\nArray 1 - {array}")

print(f"\nIndex of 30 - {array.index(30)}")

#   We can also specify conditions to the index with some optional values:

print(f"\nIndex of a array with the starting and ending indexes - {array.index(40,2,7)}")

#   Sintax of index is> (value that I want to find,start,end)

#   There are some keywords in python, like in

print(3 in array)
print(40 in array) 

#   Note that they return a boolean value


#                   Count                   #

#   count: Counts how many times a object has appeared on the list
print(f"\nCount - {array.count(30)}")


#                   Sort                    #

#   Sorts the list

array.sort()
print(f"Sorted array : {array}")

#   The sorted function, returns a new array, while the sort method doesn't

new_array = sorted(array)
print(f"\nSorted using the funcion \"sorted\": {new_array}")


#                   reverse                   #
#   The reverse method, just invert the list, making the last index become the first and so on

reverse_array = array[:]
reverse_array.reverse()
#   print(f"\nReversed array : {reverse_array}")

#   Remember that a reverse doesn't sort the array, it justs invert the order.
#   Also, you can reverse a list using the [::-1] params

print(f"\nArray is: {array}")
print(f"\nReversed list using the [::-1] : {array[::-1]}")


#                   Range                   #

#   The range funciton, generates a list based on 
#   the values that you've specified (begin->end)
print()
print(list(range(0,100))) #Creates a list that goes from 0 to 99


#                   Join                   #
#   The join method, joins something to a string,
#   follow the examples

sentence = ' ' #Created a string with a space object
sentence_b = sentence.join(['it\'s', 'really', 'hard', 'to', 'write','like','that'])
print(sentence_b)   #The space has been added to all objects

#   A better way to write the code above is:
sentence_c = ' '.join(['Wow','Much','Better'])
print(sentence_c)