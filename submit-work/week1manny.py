#####################################
#### WEEK 1 OF THE PYTHON COURSE ####
#####################################


# Explain what a variable is. What is its purpose?
# A variable in python is practically any value that the user sets which holds something within it. This can range from mere integers all the way to inputs, dictionaries, etc.
# The purpose of a variable is to be able to call upon information stored within it at any point in time.

# List the different types of Python Datatypes
# String, Boolean, Floats, Integers, etc.

# What is input function used for?
# The input function is used as a sort of entry point for a user to put in a value. This input can be set to a variable where the result can be called on any point in time. It is quite useless.

# Create a variable named color with a string value (Print the result)

color = "Blue"

# Create a variable named number with an integer value (Print the result)

number = 5
print(number)

# Create a variable named game_ended with a boolean value (Print the result)

game_ended = False
print(game_ended)

# Store an input to a variable called age. Convert the input to an integer.

age = int(input("How old are you? "))
print(age)
print(type(age))

# Hint: You can use type() to check the datatype of a variable
# (Print the result)

# Create 2 variables that store inputs from the user.
# Convert the inputs to integers.
# Add or Subtract the 2 variables and store the result in a new variable.
# (Print the result)

print("You will choose 2 numbers, make sure the first number is greater than the second. ")
n1 = int(input("Choose any number: "))
n2 = int(input("Choose another number: "))

add = n1 + n2
subtract = n1 - n2

question = input("Pick between add or subtract: ")
if question == "add":
    print(add)
else:
    print(subtract)

# Create 2 string variables and concatenate them.

a = "I love "
b = "Manny!"

print(a + b)

# There are 3 ways to concatenate strings. One is using the + operator ,f-string, and the other is using the .format() method.
# Do all three ways
# (Print the result)

Nic = "Nic is "
Cool = "Cool!"

print(Nic + Cool)

print(f"Hi there, did you know that {Nic}really freaking {Cool}")

print("Hi there, did you know that {} really freaking {}".format(Nic, Cool))




#######################################################################################################################
### Extra String Manipulation Questions (Some we might have done in session. Others I want you to research and try) ###
#######################################################################################################################
# Using the last variables you created. Print the Len of the strings

print(len(Nic))
print(len(Cool))

# Using the last variables you created. Print the first 3 characters of the strings

first3 = Nic[:3]
print(first3)

# Using the last variables you created. Print the last 3 characters of the strings

last3 = Cool[-3:]
print(last3)

# Using the last variables you created. Print the string in uppercase

print(Nic.upper())

# Using the last variables you created. Print the string in lowercase

print(Cool.lower())

# Using the last variables you created. Print the string in title case

print(Nic.title())

# Using the last variables you created. Print the string in reverse

Nic = "Nic is "[::-1]
print(Nic)

################
### Projects ###
################
# Note: Don't copy and paste code from the internet. Try to solve these problems on your own. If you get stuck, ask for help.

# Have a user input a color and a noun. Print the results of those as a superhero name.

color = input("Hey there! Pick a color for me: ")
noun = input("Would you mind giving me a noun as well? ")

name0 = print(f"Your superhero name will be {color} {noun}!")

# Create a program that asks the user for their name and age. Then print out a message to the user that tells them the year that they will turn 100 years old.

name1 = input("What is your name? ")
age = int(input("How old are you? "))

factor1 = 100
current_year = 2024

factor2 = factor1 - age

final_year = factor2 + current_year

print(f"Hey there {name1}! You will be 100 years old in the year of {final_year}.")


# Create a Tip Calculator. If the bill was $150.00, split between 5 people, with 12% tip. Each person should pay (150.00 / 5) * 1.12 = 33.6. Format the result to 2 decimal places.


bill = int(input("How much was the total bill? "))
total_people = int(input("How many people will be splitting the bill? "))
tip = int(input("What percent tip would you guys like to choose? "))

total_tip = float(tip) / 100 * bill

total_bill = total_tip + bill

cost_per_person = total_bill / total_people

print(f"Each person will be paying ${cost_per_person:.2f}")




