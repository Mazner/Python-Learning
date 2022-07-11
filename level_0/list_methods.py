#                                                                       # 
#   There are many methods to use on lists, as well, some examples:
#   Method learned in order:
#       append
#       insert
#       extend
#       pop
#       remove
#       clear
#                                                                       # 


shopping_list = [
    'Apples',
    'Oranges',
    'Yugi-oh collector\'s edition bundle, VERY RARE!!'
] 
print(f"First list : {shopping_list}")

#Adding:

shopping_list.append('Magic is not necessary')      #Adding a value at the end of the list

print(f"\nSecond list (apend) : {shopping_list}")

shopping_list.insert(1, 'Yellows')                  #With insert, we can add anywhere at the list

print(f"\nThird list (insert) : {shopping_list}")

shopping_list.extend(['One','two',3])                 #With extend, we can extend a list with multiple values

print(f"\nFourth list (Extend) : {shopping_list}")

#Removing
shopping_list.pop()     #Just like the pop of the stack, it removes the first object.
                        #But we can add the index of the list, to remove something
                        #specificaly (shopping_list).pop(1)

print(f"\nFifth list (pop) : {shopping_list}")

shopping_list.remove('Yugi-oh collector\'s edition bundle, VERY RARE!!')    #Remove the first occourence

print(f"\nSixth list (remove) : {shopping_list}")


#A good thing to notice, is that pop method, returns the value of the object removed
#The remove method doesn't

shopping_list.clear()   #This method clears all the list

print(f"\nSeventh list (clear) : {shopping_list}")
