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
