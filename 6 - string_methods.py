# #########################################################################################
# #########################################################################################
# The len() method - to calculate the number of characters in a string
# #########################################################################################
# #########################################################################################
# region

# Syntax :-
# len(string): number-int

message = "Hello World"

total = len(message)

print(total)
# output:
# 11

# endregion

# #########################################################################################
# #########################################################################################
# The upper(), lower(), capitalize() and title() method
# #########################################################################################
# #########################################################################################
# region

my_string = "welcome to python"

print(my_string.upper())  # WELCOME TO PYTHON
print(my_string.lower())  # welcome to python
print(my_string.capitalize())  # Welcome to python
print(my_string.title())  # Welcome To Python

# endregion

# #########################################################################################
# #########################################################################################
# The find() method - return the index position of a string by a given character
# #########################################################################################
# #########################################################################################
# region

# Syntax:
# <string_object>.find('p'):int

my_string = "welcome to python"

find_result = my_string.find('p')
print(find_result)  # output: 11 - index position
# ---------------------------------------------------
find_result = my_string.find('w')
print(find_result)  # output: 0 - index position
# ---------------------------------------------------
find_result = my_string.find('e')
print(find_result)  # output: 1 - grab the first 'e' character index position
# ---------------------------------------------------
find_result = my_string.find('W')
print(find_result)  # output: -1 - means we don't have an uppercase W in our string
# ---------------------------------------------------
find_result = my_string.find('welcome')
# output: 0 - will look at the first character in string which is 'w'
print(find_result)
# ---------------------------------------------------
# endregion

# #########################################################################################
# #########################################################################################
# The replace() method - place words or characters inside a string
# #########################################################################################
# #########################################################################################
# region

# Syntax:
# <string_object>.replace("old_string", "new_string"):string
# this won't effect the original string
# If replace methods finds more matching characters or words, it will replace them all

my_string = "my name is adam"

replace_result = my_string.replace("adam", "Sally")

print(replace_result)  # output: my name is Sally
print(my_string)  # output: my name is adam

replace_result = my_string.replace("m", "X")

print(replace_result)  # output: Xy naXe is adaX
print(my_string)  # output: my name is adam
# endregion

# #########################################################################################
# #########################################################################################
# The strip() method - remove whitespaces at the beginning of the string
# #########################################################################################
# #########################################################################################
# region
print("#" * 50)

my_string = "        This is python"
print(my_string)
# output:         This is python
print(my_string.strip())
# output: This is python

# endregion

# #########################################################################################
# #########################################################################################
# Using the "in" and "not in" operator- to check whether word or character exist in a string
# #########################################################################################
# #########################################################################################
# region

# Syntax:
# <look_form_stringA> in <StringA> : Boolean

title = "this is my python notes"

check_result = "python" in title
print(check_result)
# output: True
# ----------------------------------
check_result = "d" in title
print(check_result)
# output: False
# ----------------------------------
check_result = "o" in title
print(check_result)
# output: True
# ----------------------------------
print("*" * 40)
# ----------------------------------
# More Examples

print('a' in 'abc')  # output: True
print('am' in 'Adam')  # output: True
print('am' in 'Adam ')  # output: True
print('adam' in 'Adam')  # output: False

# >> not in is the opposite boolean
print('adam' not in 'Adam')  # output: True
print('a' not in 'abc')  # output: False
print('am' not in 'Adam')  # output: False


# endregion
