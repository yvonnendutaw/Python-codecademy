#returns meal costs
def tax(bill):
    bill *= 1.08
    print 'With tax: %f' % bill
    return bill
def tip(bill):
    bill *= 1.15
    print "With tip: %f" % bill
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_cost)

#calls and responds at square(10)
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)


#using parameters and arguments
def power(base,exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!

#Functions calling functions example1
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    #call the function in function1
    return one_good_turn(n) + 2

#example2

def cube(number):
    cubed = number** 3
    return cubed
def by_three(number):
    if number%3== 0:
       return cube(number)
    else:
      return False
    cube(30)


#max function
# Set maximum to the max value of any set of numbers on line 3!

maximum = max(49,42,50)

print maximum


#min function
# Set minimum to the min value of any set of numbers on line 3!

minimum = min(473,494,292)

print minimum

#absolute value ie number's distance from zero

absolute = abs(42)

print absolute

# Print out the types of an integer, a float,
# and a string on separate lines below.
print type(8)
print type(49.60)
print type('yvonne')

#example 3 on functions
def shut_down(s):
    if s == "yes":
        return "Shutting Down"
    elif s =="no":
        return "Shutdown aborted"
    else:
        return "sorry"

    #importing modules
    mport math
from math import sqrt

print sqrt(13689)

#types
def distance_from_zero(n):
   print type(n)
   if type(n)==int or type(n)==float:
      return abs(n)
   else:
       return "Nope"


#without arguments
def answer():
   x=42
   return x


    #vacation!
def hotel_cost(n):
    return 140 * n

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    total = 40*days
    if days >=7:
        total -= 50
    elif days>=3:
        total -= 20
    return total

def trip_cost(city,days):
    return hotel_cost(days) + rental_car_cost(days) + plane_ride_cost(city)
