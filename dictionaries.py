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
