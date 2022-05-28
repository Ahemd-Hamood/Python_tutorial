################################################################
# Using conditions statement with Comparison operators
################################################################
# region

a = 12
b = 44

if a < b:
    print("'a' is greater than 'b'")

# output: 'a' is greater than 'b'

a = 12
b = 44

if a > b:
    print("'a' is greater than 'b'")
else:
    print("'b' is greater than 'a'")

# output: 'b' is greater than 'a'

a = 44
b = 44

if a >= b:
    print("'a' is greater or equal than 'b'")

# output: 'a' is greater or equal than 'b'

# >>>>>>>>>>>>>>>>>>>>>>>>>
# Example
# >>>>>>>>>>>>>>>>>>>>>>>>>

temperature = 30

if temperature > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")

# output:
# it's not a hot day

if temperature >= 30:
    print("it's a hot day")
else:
    print("it's not a hot day")

# output:
# it's a hot day

if temperature <= 30:
    print("it's a hot day")
else:
    print("it's not a hot day")

# output:
# it's a hot day

if temperature != 30:
    print("it's a hot day")
else:
    print("it's not a hot day")

# output:
# it's a hot day

# endregion

################################################################
# Using logical and comparison operators
################################################################
# region
print("#" * 50)

# >> and Examples - both conditions must be true to get True

print(1 < 2 < 3)  # output: True  = 1 > 2 and 2 < 3
print(1 < 2 > 3)  # output: False = 1 < 2 and 2 > 3
print(6 < 2 < 3)  # output: False = 6 < 2 and 2 < 3
print(6 > 2 < 3 < 7)  # output: True = 6 < 2 and 3 < 7

print(2 > 1 and 3 < 2)  # output: True and False = False
print(6 > 3 and 3 < 5)  # output: True and True = True
print(2 > 3 and 3 < 5)  # output: False and True = False
print(2 == 3 and 8 < 5)  # output: False and False = False

print('h' == 'h' and 2 == 2)  # output: True and True = True

# >> We can add parentheses around each comparision
print((6 > 3) and (3 < 5))  # output: True and True = True
print((2 == 3) and (8 < 5))  # output: False and False = False


# >> or Examples = You need only one of the condition to be true to get True

print(1 == 1 or 3 == 3)  # output: True or True = True
print(1 == 1 or 3 < 1)  # output: True or False = True
print(5 >= 2 or 7 <= 1)  # output: True or False = True
print(2 != 2 or 7 <= 1)  # output: False or False = False

# >> We can add parentheses around each comparision
print((5 >= 2) or (7 <= 1))  # output: True or False = True
print((2 != 2) or (7 <= 1))  # output: False or False = False

# >> not Examples = this will change our boolean return opposite

print(not 1 == 1)  # output: True -> False
print(not 2 == 1)  # output: False -> True
print(not (2 == 1))  # output: False -> True
print(not (5 > 2))  # output: True -> False

print(not (5 > 8) and (7 > 2))  # output: True and True -> True
print(not (5 > 2) and (7 > 2))  # output: False and True -> False
print(not((5 > 2) and (7 > 2)))  # output: True -> False


print(not(5 > 8) or (7 > 2))  # output: True or True -> Ture
print(not ((5 > 8) or (7 > 2)))  # output: False -> Ture

# endregion

################################################################
# Using condition statements with logical and comparison operators
################################################################
# region

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 1 - if statement
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

prize = 100

if prize > 50:
    prize = 500

print(prize)  # output: 500

# >> Example 2 - if statement

is_login = True
if is_login:
    print("user is login")

# output: user is login

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 3 - if-else statement
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

customer_amount = 400
purchased_Item = 690

if customer_amount > purchased_Item:
    print("Transaction Complete, printing bill.....")
else:
    print("Transaction Failed, No Bill")

# output: Transaction Failed, No Bill

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 4 - if-elif-elif-else statement
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

student_grade = 99

if student_grade <= 100 and student_grade >= 90:
    print("student grade is A")
elif student_grade <= 90 and student_grade >= 80:
    print("student grade is B")
elif student_grade <= 80 and student_grade >= 70:
    print("student grade is C")
elif student_grade <= 70 and student_grade >= 60:
    print("student grade is D")
elif student_grade <= 60 and student_grade >= 50:
    print("student grade is F")
else:
    print("You are Retarded")

# output: student grade is A

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 5 - if-elif-elif-else statement
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

user_role = "admin"

if user_role == 'normal':
    print("user is has normal credentials")
elif user_role == 'super':
    print("user has super credentials")
elif user_role == 'admin':
    print("user has admin credentials")
else:
    print("Role is not available")

# output: user has admin credentials

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 6 - if-elif-elif-else statement
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person == 'George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")

# output: Welcome George!

# endregion

################################################################
# Using condition statements with logical and comparison operators - Examples
################################################################
# region
print("#" * 50)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# if temperature is greater than 30 -> then it's a hot day
# otherwise if it's less than 10 -> then it's a cold day
# otherwise -> it's neither hot not cold

temperature = 25

if temperature > 30:
    print("it's hot day")
else:
    print("it's not a hot day")


# if temperature is greater than or equal 30 -> then it's a hot day
# otherwise if it's between 0 and 29 -> then it's a cold day
# otherwise -> it's freezing

temperature = 25

if temperature >= 30:
    print("it's a hot day")
elif temperature >= 0 and temperature <= 29:
    print("it's a cold day")
else:
    print("I think its frozen")

# output:
# it's a cold day


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 2
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# if name is less than 3 characters long name must be at least 3 characters
# otherwise if it's more than 50 characters long, then name can be a maximum of 50 characters
# otherwise name looks good

# way 1

name = "adam"

if len(name) < 3 and len(name) < 50:
    print("name is OK")
else:
    print("name is not OK")

# way 2

name = "adam frank"

if len(name) < 3:
    print("name must be at least 3 characters long.")
elif len(name) > 50:
    print("name must be at a maximum of 50 characters")
else:
    print("name looks great...")

# output:
# name looks great...

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 3
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Age should be between 18 and 65]]

age = 22

if age >= 18 and age < 65:
  print("You can Drive")

# output: 
# You can Drive

# >> Or you can have your comparison without the logical operators

if 18 <= age < 65:
  print("You can Drive")

# output: 
# You can Drive


# endregion
