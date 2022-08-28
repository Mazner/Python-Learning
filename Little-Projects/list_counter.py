# Make an algorithmn that counts how many elements are in 
# the list, and sum them.



print("Put as many numbers as you'd like, and i'll print the sum of them all!")

list_size = int(input("How many elements the list will have?"))

my_list = []

i = 0
while i < list_size:
    n = int(input("Put the number > "))
    my_list.append(n)
    i += 1
sum = 0
for i in range(0,list_size):
    sum += my_list[i]
print(f"The sum equals to: {sum}")
