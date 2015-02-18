__author__ = 'Vladyslav'

# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age,is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
       print (self.name)
       print (self.age)

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)


print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.description())
