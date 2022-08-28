# Testing enumerate function


for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'Found the number 50 on the {i} position')
    else:
        print(i, char)

