#A method is a way to manipulate a string 

#let's use the capitalize and upper methods
#Capitalize(Capitalize the first letter)

quote = 'this is a non manipulated string, I swear'
print(quote.capitalize())

print(quote.upper())

print(quote.replace('non ',''))

movie = 'the dawn of the darkness'
print('\nThere\'s a nice movie I want to watch, the name is: ' + movie)
print('Oh, you mean: ' + movie.title() + '?' )
print('Stop being a weirdo...')