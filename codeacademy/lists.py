__author__ = 'Vladyslav'

##########################################################

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle =    suitcase[2:4] # Third and fourth items (index two and three)
last   =   suitcase[4:]          # The last two items (index four and five)

###########################################################

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]   # The fourth through sixth characters
frog = animals[6:]  # From the seventh character to the end

############################################################

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =   animals.index("duck") # Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

############################################################

my_list = [1,9,3,8,5,7]

for number in my_list:
    print (number*2)

#############################################################

start_list = [5, 3, 1, 2, 4]
square_list = []

for item in start_list:
    square_list.append(item**2)

square_list.sort()

###########################################################

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin'])  # Prints Puffin's room number
print (residents['Sloth'])
print (residents['Burmese Python'])

#############################################################

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
menu['Spam'] = 2.50
menu['23'] = 2.502
menu['Spa3m'] = 2.502

###############################################################

# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = "sds"

print (zoo_animals)

####################################################################

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')

####################################################################

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
    'pocket' : ['seashell', 'strange berry', 'lint'],
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']+=50

####################################################################

def print_list(x):
    for i in range(0, len(x)):
        print (x[i])


#####################################################################

range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]

####################################################################

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    print (key+' '+d[key])

###################################################################

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
#Using list slicing
message=garbled[::-1]
message=message[::2]

