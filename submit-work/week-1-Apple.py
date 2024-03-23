#####################################
#### WEEK 1 OF THE PYTHON COURSE ####
#####################################


# Explain what a variable is. What is its purpose?
# Variables can store values and information this is to help things like readability if the variable is
# named correctly
# List the different types of Python Datatypes
# String, Integer, Boolean, and Float
# What is input function used for?
# For a user to input a certain piece of information
# Create a variable named color with a string value (Print the result)
color = "Red"
print(color)
# Create a variable named number with an integer value (Print the result)
integervalue = 45
print(integervalue)
# Create a variable named game_ended with a boolean value (Print the result)
game_ended = True
print(game_ended)
# Store an input to a variable called age. Convert the input to an integer.
age = input("What is your age")
print (int(age))
# Hint: You can use type() to check the datatype of a variable
# (Print the result)
# print (int(age))
# Create 2 variables that store inputs from the user.
age1 = input("What is your age?")
mathgrade = input("What is your math grade?")
# Convert the inputs to integers.

# Add or Subtract the 2 variables and store the result in a new variable.
agemath = int(age1) + int(mathgrade)
# (Print the result)
print(agemath)
# Create 2 string variables and concatenate them.
# There are 3 ways to concatenate strings. One is using the + operator ,f-string, and the other is using the .format() method.
# Do all three ways
print("Banana" + "Apple")
food1 = "Banana"
food2 = "Apple"
combined = f"{food1} {food2}"
print(combined)
# (Print the result)
combined = "{}{}".format(food1, food2)
#######################################################################################################################
### Extra String Manipulation Questions (Some we might have done in session. Others I want you to research and try) ###
#######################################################################################################################
# Using the last variables you created. Print the Len of the strings
print(len(combined))
# Using the last variables you created. Print the first 3 characters of the strings
first_three = combined[:3]
print(first_three)
# Using the last variables you created. Print the last 3 characters of the strings
last_three = combined[-3]

print(last_three)
# Using the last variables you created. Print the string in uppercase
print(combined.upper())
# Using the last variables you created. Print the string in lowercase
print(combined.lower())
# Using the last variables you created. Print the string in title case
print(combined.title())
# Using the last variables you created. Print the string in reverse
reverse = combined [::-1]
print(combined)
################
### Projects ###
################
# Note: Don't copy and paste code from the internet. Try to solve these problems on your own. If you get stuck, ask for help.

# Have a user input a color and a noun. Print the results of those as a superhero name.
color = input("Pick a color!")
noun = input("Pick a noun!")
print(f'Your superhero name is Super {color}{noun}')
# Create a program that asks the user for their name and age. Then print out a message to the user that tells them the year that they will turn 100 years old.
age = input("What is your age?")
name = input("What is your name?")
year_turns100 = 2024 + 100 - int(age)
print(f'{name} you turn 100 in {year_turns100}')
# Create a Tip Calculator. If the bill was $150.00, split between 5 people, with 12% tip. Each person should pay (150.00 / 5) * 1.12 = 33.6. Format the result to 2 decimal places.
bill = input("What is the bill?")
tip = int(bill)/5 * 1.12
round(int(bill), 2)
print(f'Each person should pay exactly {tip}')