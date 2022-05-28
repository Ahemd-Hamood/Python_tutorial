# We are going to the input() build-in method to receive user input from our terminal

# ####################################
# 1. The input method arguments
# ####################################
# region

# input(message:string): string
# In input() method we can pass a string value, which a string message to print something on the terminal.
# our input() method return the input value as a string datatype, so you need to hold this value in some variable

# get_input = input("What is your name?")
# > What is your name? (waiting for user input)

# endregion

# ####################################
# 2. Using the input method
# ####################################
# region

name = input("what is your name ? ")
# what is your name ? adam

print("the name is " + name)
# output: the name is adam

print(type(name))
# output: <class 'str'>


# endregion

# ####################################
# 3. Example
# ####################################
# region

# We will ask user two questions, person name, favorite color and age. Then print a message like "Adam Likes White"

name = input("Enter your name? ")  # > Adam
favorite_color = input("Enter your favorite color? ")  # > red
age = input("Enter your Age please? ")  # > 22

print(name + " Likes " + favorite_color + ", and age is" + age)
# output: Adam Likes red, and age is 22

# endregion


