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
