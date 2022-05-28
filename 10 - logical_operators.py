################################################################
# Logical operators - The 'and' Operator
################################################################
# region

# >> The and operator - when two conditions con_A and con_B are True, then final output is True, otherwise false
# >> and operator is like mixing, imagine True is water, and false is poison, whenever you mix poison into water, the water become undrinkable or False
# >> In and operator all conditions must be 'True' to get 'True', otherwise 'False'

print(True and True)  # output: True
print(True and False)  # output: False
print(False and True)  # output: False
print(False and False)  # output: False

print(False and False and True)  # output: False
print(False and True and True)  # output: False
print(True and True and True)  # output: False

if True and True:
    print("Our condition is True")  # this will be executed

if True and False:
    print("Our condition is True")

if False and True:
    print("Our condition is True")

if False and False:
    print("Our condition is True")

# >>>>>>>>>>>>>>>>>>>>>>>
# Example:
# >>>>>>>>>>>>>>>>>>>>>>>

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Customer is eligible for loan")
else:
    print("Customer is not eligible for loan")

# output:
# Customer is eligible for loan

has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Customer is eligible for loan")
else:
    print("Customer is not eligible for loan")

# output:
# Customer is not eligible for loan

# endregion

################################################################
# Logical operators - The 'or' Operator
################################################################
# region
print("#"*50)
# >> The or operator - when two conditions con_A or con_B, if one of them is 'True' then the final output become 'True', if both false then our output become 'False'
# >> The or operator is like picking one good thing from multiple things, imaging True is water and False is poison, which one u will pick water-True or poison-False
# >> Definitely you gonna pick True-water, but if both are False-poison, then you have to pick False-poison because there is no other choice.
# >> In or operator, at least one condition is 'True' to get 'True', but if both 'False' then you will get 'False'

print(True or True)  # output: True
print(True or False)  # output: True
print(False or True)  # output: True
print(False or False)  # output: False

print(False or False or True)  # output: True
print(False or True or True)  # output: True
print(True or True or True)  # output: True
print(False or False or False)  # output: False

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

employee_smart = True
employee_experience = True

if employee_smart or employee_experience:
    print("You are hired")
else:
    print("We will call you later")

# output: You are hired

employee_smart = True
employee_experience = False

if employee_smart or employee_experience:
    print("You are hired")
else:
    print("We will call you later")

# output: You are hired

employee_smart = False
employee_experience = False

if employee_smart or employee_experience:
    print("You are hired")
else:
    print("We will call you later")

# output: We will call you later

# endregion

################################################################
# Logical operators - The 'not' Operator
################################################################
# region
print("#" * 50)

# The or operator simply reverse any boolean value we give it. If we give a 'True' boolean value it converts it to 'False' vice-versa
# The or operator it's like change or reverse the given output. Just think of it as in reverse way 'True' is 'False' and 'False' is 'True'

print(not True)  # output: False
print(not False)  # output: True

# >> be aware the not operator is only applied to the first condition at the left below :-

print(not True and True)  # False and True -> output: False
print(not True and False)  # False and False -> output: False
print(not False and True)  # True and True -> output: True
print(not False and False)  # True and False -> output: False

print(not True or True)  # False or True -> output: True
print(not True or False)  # False or False -> output: False
print(not False or True)  # True or True -> output: True
print(not False or False)  # True or False -> output: True

print(True or not False)  # True or True -> output: True
print(False or not False)  # False or True -> output: True

print(True and not False)  # True and True -> output: True
print(True and not True)  # True and False -> output: False

# >> Group or wrap multiple condition with parenthesis, to get their final output and reverse it

print(not (True and True))  # not(True) -> output: False
print(not (True and False))  # not(True) -> output: False
print(not (False and True))  # not(False) -> output: True
print(not (False and False))  # not(False) -> output: True

print(not (True or True))  # not(True) -> output: False
print(not (True or False))  # not(True) -> output: False
print(not (False or True))  # not(True) -> output: False
print(not (False or False))  # not(False) -> output: True

print(not (True or True or False))  # not(True) -> output: False
print(not (True and False and True))  # not(False) -> output: True

# >>>>>>>>>>>>>>>>>>>>>>>>>
# Example 1
# >>>>>>>>>>>>>>>>>>>>>>>>>

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("You can get Visa")
else:
    print("You can't get Visa")

# output:
# You can't get Visa

# >>>>>>>>>>>>>>>>>>>>>>>>>
# Example 2
# >>>>>>>>>>>>>>>>>>>>>>>>>

high_income = True
good_credit = True
student = True

if high_income and good_credit and not student:
    print("You have Loan ....")
else:
    print("Sorry you cant have Loan")

# output:
# Sorry you cant have Loan

# endregion

################################################################
# Logical operators - Mixing 'and', 'or', 'not' operators
################################################################
# region

print("#" * 50)

# >> In the following we start from left to right

print(True or False and True)
# True and True -> output: True
print(False or False and True)
# False and True -> output: False
print(False or False and True and False)
# False and True -> output: False
print(False or False and not True and False)
# False and False -> output: False

# endregion


################################################################
# Logical operators are short circuit
################################################################


high_income = False
good_credit = True
student = True

# >> python interpreter stops at high_income  because it's False, it does not bother looking for next condition this called "shot circuit"

if high_income and good_credit and not student:
    print("You have Loan ....")
else:
    print("Sorry you cant have Loan")

high_income = False
good_credit = True
student = True

# >> python interpreter stops at good_credit because it's True, it does not bother looking for next condition this called "shot circuit"

if high_income or good_credit or not student:
    print("You have Loan ....")
else:
    print("Sorry you cant have Loan")
