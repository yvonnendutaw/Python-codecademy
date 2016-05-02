# Assigning a dictionary with three key-value pairs to residents: and printing them
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

print residents['Sloth']
print residents['Burmese Python']

#Adding items to the disctionaries
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['fries'] = 100
menu['fish'] = 89
menu['beef'] = 72

print "There are " + str(len(menu)) + " items on the menu."
print menu

#deleting the keys and their values
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
zoo_animals['Rockhopper Penguin'] = ['Gen']


print zoo_animals


#removing items from a list
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print backpack


#sorting-adding a number to the total
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket']=['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']+=50


#printing items in lists
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for names in ["Adam","Alex","Mariah","Martine","Columbus"]:
    print names
    #printing items in dictionaries

webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]

#print loop item in list
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0:
        print number

#fizzbuzz
# Write your function below!
def fizz_count(x):
    count = 0
    for n in x:
        if n == "fizz":
            count = count + 1

    return count

#string looping
for letter in "Codecademy":
    print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter

#shopping cart
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}
#for loop that prints the three statements
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

total = 0
for key in prices:
    prices[key] * stock[key]
    total +=  prices[key] * stock[key]
    print total

#making a purchase
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for n in food:
        total = total + prices[n]
    return total

#stocking out
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for n in food:
        if stock[n] > 0:
            total = total + prices[n]
            stock[n] -= 1
        else:
            total = total
    print total
    return total

#for the record
students = [lloyd, alice, tyler]
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

print lloyd["name"]
print lloyd["homework"]
print lloyd["quizzes"]
print lloyd["tests"]

print alice["name"]
print alice["homework"]
print alice["quizzes"]
print alice["tests"]

print tyler["name"]
print tyler["homework"]
print tyler["quizzes"]
print tyler["tests"]


#getting the average
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total) / float(len(numbers))
    return total



 #just weight and see

def get_average(student):
    homework = average(student["homework"])* 0.1
    quizzes = average(student["quizzes"])* 0.3
    tests = average(student["tests"])* 0.6

    avrg = homework + quizzes + tests
    return avrg

#getting letter
def get_letter_grade(score):
    if score>= 90:
        return 'A'
    elif score>= 80:
        return 'B'
    elif score>= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print get_letter_grade(get_average(lloyd))
print get_letter_grade(get_average(alice))
print get_letter_grade(get_average(tyler))

students=[lloyd, alice, tyler]

def get_class_average(students):
    results=[]
    for student in students:
        results.append(get_average(student))
    return average(results)
