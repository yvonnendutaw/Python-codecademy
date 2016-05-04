#while counts to 9
count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count

while count < 10:
    print "Hello, I am a while and count is", count
    count +=

    #how the loop checks for condition
    loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False

    #using while with arithmetic operations
    num = 1

while num <= 10:  # Fill in the condition
    print num ** 2
    num += 1

    #using while to check simple errors
    choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")



#game using while
m random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

while guesses_left > 0:
    print 'You got %s guesses left' % guesses_left
    guess = int(raw_input('Guess a number (1-10):'))

    if guess == random_number:
        print 'You win!'
        break
    guesses_left -= 1
else:
    print 'You lose.'

    #hobbies
    hobbies = []

# Add your code below!
hobby = raw_input("What is your hobby?")
for i in range(3):
    hobbies.append(hobby)

    ##looping through a string
    thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!
for c in word:
    print c

    ##replacing char in strings
    phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == "A" or char == "a":
        print "X",
    else:
        print char,

        ##looping through lists
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!
for num in numbers:
    print num**2


##looping through dictionaries and printing the keys and values
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
 print key, d[key]

