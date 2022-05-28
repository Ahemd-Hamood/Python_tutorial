################################################################
# Comparison operators - >, <, >=, <=, ==, !=
################################################################
# region

# >>>> Comparison Operators :-
# we use them to return boolean values the comparison operator are :-

# A. Equal Operator: a == b :-
# If the 'a' and 'b' are equal, then the condition become true, otherwise it become false
# -------------------------------------------------------------------------------------------------
# B. Not Equal Operator a != b :-
# If the 'a' and 'b' are not equal, then the condition become true, otherwise it become false
# -------------------------------------------------------------------------------------------------
# C. Greater than Operator: a > b :-
# if 'a' value is greater than b value, then the condition become true, otherwise it become false
# -------------------------------------------------------------------------------------------------
# D. Less than Operator: a < b
# if 'a' value is less than 'b' value, then the condition become true, otherwise it become false
# -------------------------------------------------------------------------------------------------
# E. Greater than or Equal Operator: a >= b
# if 'a' value is greater than or equal 'b' value, then the condition become true, otherwise it become false
# -------------------------------------------------------------------------------------------------
# F. Less than or Equal Operator: a <= b
# if 'a' value is less than or equal 'b' value, then the condition become true, otherwise it become false

# Be aware of the following :-
# a == b  # output : True
# a = b   # output : TypeError: 'a' is an invalid keyword argument for print() - single "=" is called assignment

print(10 < 3)  # output: True
print(10 >= 3)  # output: True
print(10 < 20)  # output: True
print(10 <= 20)  # output: True
print(10 == 10)  # output: True
print(10 != 10)  # output: False
print(10 <= 10)  # output: True

# >> Values with different types are consider not equal like the following :-

print(10 == '10')
# output: False
print(10 != '10')
# output: True
print('10' == '10')
# output: True
print('12' == '10')
# output: False
print(10 == 10)
# output: True
print(10 != 10)
# output: False

# >> We can use comparison operator with strings, our comparison looks at the first character of out string and compare it by the alphabet order :-

print("apple" > "bag")  # output: False --> 'a' is less than 'a'
print("apple" < "bag")  # output: True --> 'b' is bigger than 'a'

print("bag" == "Bag")  # output: False

# to get th numeric representation of our letter alphabet we use the ord() function :-
print(ord("a"))  # output: 97
print(ord("b"))  # output: 98
print(ord("B"))  # output: 66

# endregion
