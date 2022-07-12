#   We can upack a list, this means, we can assign individual
#   variables to individual of the list, like this:

a,b,c,*the_rest,the_last_obj = [1,2,3,4,5,6,7,8,9,10] #a = 1, b = 2, c = 3

print(f"\n{a}\n{b}\n{c}\n{the_rest}\n{the_last_obj}")