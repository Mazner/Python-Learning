some_list = ['a','b','c','d','e','d','e',
            'f','g','a','e']

list_size = len(some_list)

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)


print(duplicates)