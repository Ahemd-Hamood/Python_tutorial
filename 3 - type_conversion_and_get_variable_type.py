# ####################################
# 1. Type conversion
# ####################################
# region

# The input method takes user input and return it as a string value type
# when you enter a number, our input method will treat this number as string like this '3'
# We will use a type conversation build-in methods like :- i
# - int() which convert string into integer number
# - float() which convert string into integer number
# - bool() which convert string, number, list, tuples into boolean
# - str() which convert number into string

# >> Problem

# birth_year = input("You Birth Year please? ")
# age = 2022 - birth_year
# print(age)

# TypeError: unsupported operand type(s) for -: 'int' and 'str'

# >> Solution 1 - wrap int() around birth_year variable

birth_year = input("You Birth Year please? ")  # > 1992

age = 2022 - int(birth_year)
print(age)  # output: 30

# >> Solution 2 - or wrap int() around the input() method

birth_year = int(input("You Birth Year please? "))  # > 1992

age = 2022 - birth_year
print(age)  # output: 30

# endregion

# ####################################
# 2. Get variable value type
# ####################################
# region

# We have a build-in method called type(), which you can pass to it, your variable value, to get it's type

name = "adam"
print(type(name))
# <class 'str'>

age = 23
print(type(age))
# <class 'int'>

rate = 3.8
print(type(rate))
# <class 'float'>

# We can check the type of user input, as we know th input method return for us value as a string data type

birth_year = input("You Birth Year please? ")  # > 1992
print(type(birth_year))  # <class 'str'>


birth_year = int(input("You Birth Year please? "))  # > 1992
print(type(birth_year))  # <class 'int'>


# endregion

# ####################################
# 3. Example
# ####################################
# region

# Ask the user their weight (in pounds), convert it to kilograms and print on the terminal

weight_in_pound = input("Enter your weight in pound? ")

convert_pound_to_kilogram = float(weight_in_pound) * 0.453

print("You weight in Kg as float is: " + str(convert_pound_to_kilogram))
print("You weight in Kg as integer is: " + str(int(convert_pound_to_kilogram)))

# output:
# Enter your weight in pound ? 200
# You weight in Kg as float is: 90.60000000000001
# You weight in Kg as integer is: 90


# endregion
