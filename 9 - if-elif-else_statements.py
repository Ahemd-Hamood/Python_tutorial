################################################################
# If-elif-else statement
################################################################
# region

# if statement allow us to make decisions based on some conditions
# if condition true we are going to do certain things otherwise we're going to do other.

# >> If statement

if True:
    print("Condition is true")

if False:
    print("Condition is false")

# >> if-else statement

if True:
    print("Condition is true")
else:
    print("Condition is true")

print("#" * 50)
# >> if-elif-else statement - second condition
# we use elif to specify another condition in case the previous condition is false

if False:
    print("Condition is true")
elif True:
    print("Condition is true")
else:
    print("all condition above are false")

# >> if-elif-else statement - many conditions

# if condition_1:
#     print("Condition is true")
# elif condition_2:
#     print("Condition is true")
# elif condition_3:
#     print("Condition is true")
# elif condition_4:
#     print("Condition is true")
# elif condition_5:
#     print("Condition is true")
# else:
#     print("all condition above are false")

print("#" * 50)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example - if-else :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

is_hot = True

if is_hot:
    print("it's hot today")
    print("Drink plenty of water")
else:
    print("It's cold today")
    print("You better wear warm clothes")

print("Have a nice day")

# output:
# it's hot today
# Drink plenty of water
# Have a nice day

print("#" * 50)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example - if-elif-else :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

is_hot = False
is_cold = True

if is_hot:
    print("it's hot today")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold today")
    print("You better wear warm clothes")
else:
    print("It's a lovely day")

print("Have a nice day")

# output:
# It's cold today
# You better wear warm clothes
# Have a nice day

print("#" * 50)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example - if-elif-else :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

is_hot = False
is_cold = False
is_normal = True

if is_hot:
    print("it's hot today")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold today")
    print("You better wear warm clothes")
elif is_normal:
    print("It's normal today")
    print("wear whatever you like")
else:
    print("Unknown Weather")

print("Have a nice day")

# output:
# It's normal today
# wear whatever you like
# Have a nice day

print("#" * 50)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example - if-elif-else :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

is_hot = True
is_cold = False
is_normal = False

if is_hot:
    print("it's hot today")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold today")
    print("You better wear warm clothes")
elif is_normal:
    print("It's normal today")
    print("wear whatever you like")
else:
    print("Unknown Weather")

print("Have a nice day")

# output:
# it's hot today
# Drink plenty of water
# Have a nice day

# endregion

################################################################
# If-elif-else statement - Example
################################################################
# region

house_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price

print(f"down_payment: {down_payment} ")

# output:
# down_payment: 100000.0

# endregion
