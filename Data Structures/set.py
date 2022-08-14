# A set is a collection of UNIQUE items 

my_set = {1,2,3,4,5,5,6,7,7,8,10,12,12} #The set only contains 1 value of each object, excludind duplicates

print(my_set)

my_set.add(142)

print(my_set)

# Transforming a list on a set

my_list = [1,2,4,5,6,2,4,3,6,7,83,2,4]
print()
print(my_list)
print('\nNote that the list contains duplicates\nNow see the list transformed to a set:\n')
print(set(my_list))

# A set doesn't have a index predefined
new_set = my_set.copy
print(12 in my_set)

# Set methods:

set_1 = {1,2,3,4}
set_2 = {3,4,5,6}

print(set_1.difference(set_2)) # Show what appear on set 1 but doesn't appear on set 2
print(set_2.difference(set_1)) # Show what appear on set 2 but doesn't appear on set 1

#set_1.difference_update(set_2) # Removes the elements that appears on set 1 and 2
#print(set_1)

print(set_1.intersection(set_2)) # Shows the intersection of set 1 and 2