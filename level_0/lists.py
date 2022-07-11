# lists are like arrays (but there are differences)
# let's see how they work:

li = ['Here can have ', 'any value ', 232, 43.2]

print(f"And we can access them using the indexes\n{li[0]}{li[1]}\n{li[2]}\n{li[3]}")

# list slicing 
# On list slicing, there are some peculiarities
# for instance:

shopping_cart = [
    'Banana',
    'Grapes',
    'Pepper'
]
print(shopping_cart) 

shopping_cart[0] = 'Crackers'   #We can reassing values

print(shopping_cart)

new_cart = shopping_cart[0:2]   #we can assign the values that we want to send to the new cart
new_cart[0] = 'Pineapple'       #Editing the value of index 0 to Pineapple

print(new_cart)
print(shopping_cart)


new_cart = shopping_cart        #pay attention to the difference on the declarations
new_cart[0] = 'Coke'
print(f"Shopping cart - {shopping_cart}")
print(f"New_cart - {new_cart}")  

#   Both of them now have the same value, because we are making
#   new_cart point to shopping cart, so the values are changed 
#   on the "shopping_cart", because of the declaration

#   If we want to copy the list to another list, use the [:]

new_cart = shopping_cart[:]     #Now we've coppied the entire list to a new one

new_cart[0] = 'Oranges'
new_cart[1] = 'Cheese'
new_cart[2] = 'Bread'

print(f"\nNew cart and shopping cart using the\nnew_cart = shopping_cart[:] assign:\n\n*new_cart - {new_cart}\n*shopping_cart - {shopping_cart}")