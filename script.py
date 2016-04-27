#lists are datatypes
zoo_animals = ["pangolin", "cassowary", "sloth","cat" ];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

    #prints 2nd and 3rd item on list
    numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1]+ numbers[3]

#replacing list items
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3]="dog"
