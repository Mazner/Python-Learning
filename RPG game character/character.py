#The program bellow states that a character on a RPG game has a weapon, armor and a inventory
#It also prints his inventory and if no inventory is detected, it shows that there's no inventory.

character = {
    'weapon_equipped' : ['Bow of Jewel'],
    'armor_equipped' : ['Leather boots', 'Leather headhgear', 'Leather chestplate','Leather pants'],
    'health_points' : 100,
    'is_alive' : True,
    'inventory' : ['Bow of Jewel','Leather boots', 
                   'Leather headhgear', 'Leather chestplate',
                   'Leather pants', 'Health potion', 'Stamina potion']
}

print(character.get('inventory','no items on the player\'s inventory')) #get is a method


