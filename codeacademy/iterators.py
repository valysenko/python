__author__ = 'Vladyslav'

############################

my_dict = {
    "Name": "Guiddo",
    "Age": 56,
    "BDFL": True
}
print (my_dict.keys())
print (my_dict.values())

for key in my_dict:
    print (key, my_dict[key])

##############################
#

evens_to_50 = [i for i in range(51) if i % 2 == 0]
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
even_squares = [x**2 for x in range(1,11) if x%2==0]
cubes_by_four = [x**3 for x in range(1,11) if (x**3)%4==0]
threes_and_fives = [x for x in range(1,16) if x%3==0 or x%5==0]

###############################

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print (l[2:9:2])

#######################################3

to_five = ['A', 'B', 'C', 'D', 'E']

print (to_five[3:])
# prints ['D', 'E']

print (to_five[:2])
# prints ['A', 'B']

print (to_five[::2])
# print ['A', 'C', 'E']

########################################

my_list = range(1, 11)
backwards = my_list[::-1]

#########################################

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14:1]

#########################################


movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print (movies.items())
