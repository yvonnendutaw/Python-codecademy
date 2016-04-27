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


#adding late arrivals and printing oout list length
suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("Clothes")
suitcase.append("Sunscreen")
suitcase.append("Sandals")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase


#slicing lists
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]# The fourth through sixth characters
frog = animals[6:]              # From the seventh character to the end
