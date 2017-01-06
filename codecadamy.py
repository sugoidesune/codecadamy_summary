#everything written after a # is considered a comment and not executed as code.
""" Tripple quotation marks
allow for
multy line comments"""

print "Welcome to Python!"  #print outputs its content to the user- in this case a string. which you can recognise by the quotation marks
#if you use quotation marks inside the print message you can use single quotation marks ' or tripple ''' or tripple double """

################################----Variables----##########################################
#these are variables - they can store values
my_variable = 10
my_int = 7
my_float = 1.23
my_bool = True

#they can also store strings
my_name = "Pikachu"
my_goal = "The very best"


#you can reassign variables. my_int is equal to 7 in the beginning 
my_int = 7
my_int = 3 # this changes it to 3
print my_int # this will now print 3 instead of 7



################################----Functions----############################################


#the following is a basic function but as it is now, it is wrong
#indentation is very important - everything is on the same "column" in this one... take a look at the next one
def spam():
eggs = 12 
return eggs 
        
print spam() 



# the following is the same function but has proper indentation:
def spam():                         # the functions name is "spam"
    eggs = 12                       # its job is to create the variable eggs and set it equal to 12
    return eggs                     # everytime you CALL the function "spam" it will RETURN the variable "eggs" as answer.
        
print spam()                        # so when you print the function spam, it will show what has been returned - the variable "eggs" and eggs equals 12 so it will print "12"


####################################----Math----############################################

# these are variables named after the calculations they contain
addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9
exponentiation = 10 **2 #if you use multiple in 2**3**4 the outside one 4 is used first. use brackets to counteract that (2**3)**4
modulo = 10%9 # returns remainder from division. in this case 10%9 = 1 


#this is how a function can do math
def count_to(): # it defines 
 count_to = 123124124124 + 123123123124124124
 return count_to

print count_to()


#######################----Meal Cost Calculator----#########################################

#the variables
meal = 44.50
tax = 0.0675
tip = 0.15

#the calculations
meal = meal + meal * tax
total = meal + meal * tip

print("Your total meal costs %.2f $" % total) # printing the variable total inside a string
# %.2f this prints the (floating point) number to 2 digits after the decimal point.
# % in this case is a String Formating Operator just so you know the name


##########################----Strings are Indexed----########################################

#Each character in a string is assigned a number. This number is called the index. 
"""
This is how strings are being indexed.
+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5
"""

fifth_letter = "MONTY"[4]

print fifth_letter # This will now print the fifth letter of "MONTY" which is "Y". in python you start counting with 0

t
###########################----String Methods----############################################

parrot = "Norwegian Blue"
print len(parrot) # gprints the length of the string
print parrot.lower() # prints the string but with only lower case letters. important doesnt change the actual string!
print parrot.upper() # prints the string but with only upper case letters. important doesnt change the actual string!

pi = 3.14
print str(pi) # turns the variable into a string.


###############################----Printing ----############################################

word1 = "Spam"
word2 = "and"
word3 = "eggs"
space = " "
print word1 + space + word2 + space + word3 # adding is fine

print "The value of pi is around " + str(3.14) # dont forget to turn the number into a string

#:::::::::::::::::::::::::::::::::::::::::: fancy printing insertion
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
# in this case % is a String Formating Operator just so you know the name

###################----Code with user input ----##############################

name = raw_input("What is your name?") # raw_input prints a string and waits for user input.
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite pokemon?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite pokemon is %s." % (name, quest, color)

#################---- Conditional Functions ----- #########################
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

#####################---- comparing values------ ###############

Equal to (==)
Not equal to (!=)
Less than (<)
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=)

# comparing values returns True or False

bool_one = 3 < 5 # this is True
bool_two = 3**4 <8 # this is False
bool_two = "Loveme" == "Loveme"   # you can compare strings too

#######################---- Boolean Operators-----###################

# variables can be true or false

bool_one = True
bool_two = False


and, which checks if both the statements are True;
or, which checks if at least one of the statements is True;
not, which gives the opposite of the statement.

#Result list
"""
     Boolean Operators
------------------------   
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

########### boolean operators and##############
"""
The boolean operator "and" returns True when the expressions on both sides of "and" are true
1 < 2 and 2 < 3 is True;
1 < 2 and 2 > 3 is False."""


"""The boolean operator or returns True when at least one expression on either side of or is true. For example:

1 < 2 or 2 > 3 is True;
1 > 2 or 2 > 3 is False. """

"""The boolean operator not returns True for false statements and False for true statements.

not False will evaluate to True, while 
not 41 > 40 will return False."""

bool_one = False or not True and True  #False	

bool_two = False and not True or True  #True

bool_three = True and not (False or False) #True

bool_four = not not True or False and not True    #True

bool_five = False or not (True and True)      #False

###############################################################################
#############################---UNIT 5---######################################
###################-----List and Dictionaries-------###########################

zoo_animals = ["pangolin", "cassowary", "sloth", "pikachu" ];

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0] #prints pangolin
	print "The fourth animal at the zoo is the " + zoo_animals[3] #prints pikachu

zoo_animals[2] = "cow" #reassigning list index- this will now print "cow" instead of sloth

################DELETING FROM LIST#####################
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")
	
#________________________Numbers___________________________________	
numbers = [5, 6, 7, 8]
print numbers[0] + numbers[2] # adds numbers 5 and 7

#_________________________________ADD ITEMS TO LIST


new_zoo = [] # you can append to an empty list.
new_zoo.append("bisasam") # adds bisasam to the list
list_length = len(new_zoo) # length of the list.
print "There are %d animals in the Zoo." % (list_length)

first  = new_zoo[0:2] #stores first and second animal ( the 0th and the 1st but not 2nd)

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]              # Third and fourth items (index two and three)
last   = suitcase[4:6]               # The last two items (index four and five)

animals = "catdogfrog"
first  = animals[:3]   # The first three characters of animals
second  = animals[3:6]               # The fourth through sixth characters
third = animals[6:]
print first,second,third #prints cat,dog,frog
# From the seventh character to the end

#______________________________INSERT ITEMS IN SPECIFIC PART OF LIST_________

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =  animals.index("duck")  # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation
print duck_index

#----------------------------FOR LOOPS
my_list = [1,9,3,8,5,7]

for number in my_list:
    print number*2
    # Your code here
#_____________________FOR LOOPS, SQUARING, SORTING LIST____________
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
    square_list.append(number **2)
    
square_list.sort()

print square_list
#___________________________________________DICTIONARIES_____________________-
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

#____________________________MUTING DICTIONARIES_______________________
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# adding some dish-price pairs to menu!
menu["sausage"] = 4.99
print "There are " + str(len(menu)) + " items on the menu." #items in the menu

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',}

del zoo_animals['Unicorn'] #deleting entry
zoo_animals['Sloth'] = "Lonely Animals" # changing value of entry

#_________________________COMBINING DICTIONARIES WITH LISTS___________________-
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code her
inventory['pocket']=["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] =inventory["gold"]+50
print inventory
print inventory["pocket"]

#__________________________________

############################## FOR loops and Lists and Dictionaries #####################

#printing from lists
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for item in names:
    print item

#printing from dictionaries
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
	"Baa" : "The sound a goat makes.",
	"Carpet": "Goes on the floor.",
	"Dab": "A small amount."
}

for key in webster:
    print webster[key]



#conditional for loops
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for crap in a:
    if crap % 2 == 0:
        print crap

	
	
#using lists as input for functions
x =["fizz","cat","fizz"]

def fizz_count(fizzlist):
    number_of_fizzes=0
    print number_of_fizzes
    for fizzes in fizzlist:
        if fizzes == "fizz":
            print "fizz +1"
            number_of_fizzes = number_of_fizzes +1
    return number_of_fizzes

number_of_fizzes=fizz_count(x)
print number_of_fizzes



#looping through strings

for letter in "Codecademy":
    print letter
    
# another example
word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter


#Groceries Store
#Dictionaries and Loops

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for shit in stock:
    print "%s"%(shit)
    print "price: %s"%( prices[shit])
    print "stock: %s" %(stock[shit])

#Total inventory - how much is everything i got worth

for cash in prices:
    total= total + (prices[cash] * stock[cash])
	print total


#shopping list and total bill
shopping_list = ["banana", "orange", "apple"]


def compute_bill(food):
    total = 0 # start with a total of 0
    for item in food: # for every item in the shopping list
        total += prices[item] # for every item in the food list, add the price of the that item from the prices list.
    return total # show the total

#previous function developed further
# limit the purchase to the amount of items left in stock.

def compute_bill(food):
    total = 0
    for item in food:
        #print item, stock[item]
        if stock[item] > 0 : if theres more than
            stock[item] -= 1
            print item, prices[item]
            total += prices[item]
    return total












































































































