__author__ = 'Vladyslav'

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print ("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print ("With tip: %f" % bill)
    return bill

def biggest_number(*args):
    print (max(args))
    return max(args)

def smallest_number(*args):
    print (min(args))
    return min(args)

def distance_from_zero(arg):
    print (abs(arg))
    return abs(arg)

def distance_from_zero(n):
    if type(n)==int or type(n)==float:
        return  abs(n)
    else:
        return "Nope"

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


print (type(42))
print (type(4.2))
print (type('spam'))