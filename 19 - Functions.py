################################################################
##################### Defining Function ########################
################################################################
# region

# We use function to break our code into small re-usable pieces, to create function we start with the 'def' keyword.
# Next we give our function a name, make sure that you function name is meaningful descriptive.
# to write function name we use lower case letters, and underscore to separate multiple word.
# After the function name we add open-close parenthesis (), in between we add a list of parameters for later
# After that we add a colon ':', then we press Enter to get indentation which mean you entered your function body
# All the following statements will belong to this function. then we remove the indentation and break two line after the function to keep the code clean
# Finally we call our function, by specifying the function name followed by open-close parenthesis ().

def greet_user():
    print("Hey there")
    print("Welcome to Python")


# We call our function
greet_user()

# output:
# Hey there
# Welcome to Python

# endregion

################################################################
############## Function Parameters/Arguments ###################
################################################################
# region

# Our function can take an input, we can pass inputs or 'parameters' to our function in between parenthesis we pass a list of 'parameters'.
# We will add two 'parameters' for example first_name and last_name. Now when we call our function we must supply those parameters as 'arguments'.
# A. Create function with parameter
# B. call function with and pass arguments

# >> Define function with two parameters


def get_name(first_name, last_name):
    print(f"Welcome {first_name} {last_name}")


# >> Now we call our function and pass two arguments value to it :-
get_name("Adam", "White")
# output:
# Welcome Adam White

# get_name()
# output:
# TypeError: get_name() missing 2 required positional arguments: 'first_name' and 'last_name'

# get_name("Adam")
# output:
# TypeError: get_name() missing 1 required positional argument: 'last_name'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> function by default return None
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print(get_name("Adam", "White"))
# output:
# Welcome Adam White
# None

# endregion

################################################################
############### Function that return a value ###################
################################################################
# region

# We can return a value from our function, simply by using the 'return' keyword inside our function


def greet_user(name):
    return f'Welcome {name}'


message = greet_user("Adam")

print(message)
# output:
# Welcome Adam

print(greet_user("David"))
# output:
# Welcome David

# >>>>>>>>>>>>>>>>>>>>>>
# >> An Example
# >>>>>>>>>>>>>>>>>>>>>>


def cal_total(num1, num2): return num1 + num2
def merge_name(f_name, l_name): return f_name + ' ' + l_name
def print_info(name, age): return f'{name} is {age} years old.'


total = cal_total(1, 4)
print(total)
# output:
# 5

print(merge_name("Adam", "Sam"))
# output:
# Adam Sam
print(print_info("Adam", 23))
# output:
# Adam is 23 years old.

# endregion

################################################################
################### Function Key Arguments #####################
################################################################
# region

# We can specify the key name of our parameter function while calling it.
# This is helpful if you want pass argument in different order, instead of the default parameter order.


def get_name(first_name, last_name):
    return f"Welcome {first_name} {last_name}"


print(get_name("Adam", "David"))
# output: Welcome Adam David
print(get_name("Adam", last_name="David"))
# output: Welcome Adam David
print(get_name(first_name="Adam", last_name="David"))
# output: Welcome Adam David
print(get_name(last_name="David", first_name="Adam"))
# output: Welcome Adam David

# >> If you use key argument at first, then you must use it for other arguments after it or you gonna get an error

# print(get_name(first_name="Adam", "David"))
# output: SyntaxError: positional argument follows keyword argument

# endregion

################################################################
################### Default Arguments ##########################
################################################################
# region

# We know that all the parameters that you define for a function are required by default, we can make these parameter optional
# just by assigned our parameter while defining our function like this def my_fun(name="adam"): here some example.

# As you see below


def increase_num(number, by=1):
    return number + by


# >> Here we provide both parameters we want to increase out number by +3
print(increase_num(1, 3))  # output: 4
print(increase_num(1, 10))  # output: 11

# >> Without defining the second argument, the default argument will take place and assign the 'by' variable with a value of 1
print(increase_num(1))  # output: 2 --> similar to this increase_num(1, 1)
print(increase_num(6))  # output: 6 --> similar to this increase_num(6, 1)

# >> Note: Once you assign you first parameter with a default argument, you must do the same with all parameter that comes after, otherwise you will get an Error "non-default argument follows default argument"
# def bad_fun(num=1, by): return ""             --> Error "non-default argument follows default argument"
# def bad_fun(num=1, by=1): return ""           --> OK
# def bad_fun(num, by=1, another): return ""    --> Error "non-default argument follows default argument"
# def bad_fun(num, by=1, another=3): return ""  --> Ok

# >>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>


def display_customer(name, age, title="Mr"):
    return f"{title}.{name} your age is {age}"


result = display_customer("Adam", 34, "Boss")
print(result)  # output: Boss.Adam your age is 34
result = display_customer("Adam", 34)
print(result)  # output: Mr.Adam your age is 34

# endregion

################################################################
############## *args a collection of arguments #################
################################################################
# region

# We use *args to take unlimited or a collection number of arguments, sometime you need to pass more than one argument.
# When you create a function you define a number of parameters that will match the number of argument that we pass while calling our function.
# sometime you want to define a single parameter/variable that receive a collection of arguments.
# to do that we define our parameter variable with any name and we prefix it with an asterisk/start like this -> def my_fun(*numbers):
# The *number will receive a number of arguments and store them into tuples (arg1, arg2, arg3, ....) tuples are a collection of objects
# You must place your *arg as the last parameter, otherwise you gonna get an error 'missing 1 required keyword-only argument'


def func_numbers(*numbers):
    print(numbers)


func_numbers(1, 2, 3, 4, 5)
# output:
# (1, 2, 3, 4, 5)


def func_numbers(num1, num2, *remaining):
    print(num1)
    print(num2)
    print(remaining)


func_numbers(1, 2, 3, 4, 5, 6, 7)
# output:
# 1
# 2
# (3, 4, 5, 6, 7)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> You can't do the following
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def func_numbers(num1, *remaining, num2): return ""
def func_numbers(*num1, num2, num3): return ""

# func_numbers(1,2,3,4,5,6)
# TypeError: func_numbers() missing 1 required keyword-only argument: 'num2'
# func_numbers(1,2,3,4,5,6)
# TypeError: func_numbers() missing 2 required keyword-only arguments: 'num2' and 'num3'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - Iterate thru *args using for-in loop :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def print_numbers(*numbers):
    for item in numbers:
        print("number:", item)


print_numbers(1, 2, 3, 4, 5)
# output:
# number: 1
# number: 2
# number: 3
# number: 4
# number: 5

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - Iterate thru *args and get total :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def total_numbers(*numbers):
    total = 0
    for item in numbers:
        total += item
    return total


result = total_numbers(1, 2, 3, 4, 5)

print("Total:", result)

# output:
# Total: 15

# endregion

################################################################
########## **args a collection of key-value arguments ##########
################################################################
# region

# **args with pass keyword arguments where name=value, Instead of passing values into pre-defined variable parameters function.
# We can create a collection of new variable names with their value as key=value pairs, and store them or pack them into a dictionary {"key": "value"}.


def user_info(**info):
    print(info)


user_info(id=1, name="adam", age=22, gender="male")
# output:
# {'id': 1, 'name': 'adam', 'age': 22, 'gender': 'male'}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Note: don't start with **args parameter, the following are not allowed :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def user_info(**other, name): return ""
# def user_info(**other, name, age): return ""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def customer_info(name, age, **other_info):
    print(f"Customer name: {name}, age is {age}")
    print("Additional Information:", other_info)


customer_info("Adam", 33, mobile_no="987-986-345",
              gender="male", account_balance=1200.00)

# output:
# Customer name: Adam, age is 33
# Additional Information: {'mobile_no': '987-986-345', 'gender': 'male', 'account_balance': 1200.0}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - Get/Access individual key value :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def user_info(id, **info):
    print(id)
    # print(info.name)  --> 'dict' object has no attribute 'name'
    print("name:", info['name'])
    print("age:", info['age'])


user_info(1, name="adam", age=44)
# output:
# 1
# name: adam
# age: 44

# endregion
