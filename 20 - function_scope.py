################################################################
########## Function Scope - Local variable #####################
################################################################
# region

# Scope refers to region of the code where a variable is defined. when you define variables inside a function,
# the variable only can be accessed within that function, you can't access it outside that function we call these variable 'local variables'
# The local variables have a short lifetime, python allocate memory reference to local variable, when finish executing our function,
# the local variable will be released from memory and get garbage collected

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. >> Here we define a variable that only can be accessed inside the function scope,
# our variable only exist inside that function, this variable is called 'local variable' scope
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from email import message


def greet():
    message = "hey everyone"  # // local variable
    print(message)


greet()
# output:
# hey everyone

# print(message)
# output:
# NameError: name 'message' is not defined
# this means our message variable does not exist in the global scope

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# B. >> Parameters also are local variables, only exist or accessible within it's function
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# // name and age are local variable only exist inside the get_name() function.
def get_name(name, age):
    print(name)
    print(age)


get_name('Adam', 33)
# output:
# Adam
# 33

# print(name) // output: NameError: name 'name' is not defined
# print(age) // output: NameError: name 'age' is not defined

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# C. >> similar variable name within different function are in different scope so they are not the same
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def greet():
    message = "message A"
    name = "Adam"
    print(message)
    print(name)


def bye():
    message = "message B"
    print(message)
    # print(name) # NameError: name 'name' is not defined


greet()
# output:
# message A
# Adam

bye()
# output:
# message B

# print(message)
# output:
# NameError: name 'message' is not defined

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# D. >> define another variable inside our function with the same name as the parameter
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def greet(message):
    message = "message A"
    print(message)


greet("parameter message")
# output:
# message A

# print(message)
# output:
# # NameError: name 'message' is not defined

# endregion

################################################################
########## Function Scope - Global variable #####################
################################################################
# region

# global variable are accessible from anywhere, the local variable with the same name as global variable can overwrite the variable

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. >> local variable can overwrite global variable :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

message = "global"  # here global variable


def greet():
    message = "local"  # create a new local variable inside the greet() function
    print("within function:", message)


greet()
# output:
# within function: local

print("outside function:", message)
# output:
# outside function: global

# endregion

################################################################
########## Function Scope - Global keyword #####################
################################################################
# region

# A. You can modify the global variable inside our function - BAD Practice

message = "global"  # here global variable


def greet():
    global message  # create a new local variable inside the greet() function
    message = "local"
    print("within function:", message)


greet()
# output:
# within function: local

print("outside function:", message)
# output:
# outside function: local


# endregion

################################################################
###### Function Scope - Enclosing function locals ##############
################################################################
# region

###########
# Example 1
###########

name = "this is a Global variable String"


def greet():
    print(f"Hello {name}")  # this is a Global variable String

    def another_greet():
        print(f"Hello {name}")  # this is a Global variable String

    another_greet()


greet()

# output:
# this is a Global variable String
# this is a Global variable String

###########
# Example 2
###########


name = "this is a Global variable String"


def greet():
    name = "Sammy"  # enclosing - this variable only available locally inside greet() and another_greet functions
    print(f"Hello {name}")  # Hello Sammy

    def another_greet():
        print(f"Hello {name}")  # Hello Sammy

    another_greet()


greet()

# output:
# Hello Sammy

###########
# Example 3
###########


name = "this is a Global variable String"


def greet():
    print(f"Hello {name}")  # this is a Global variable String

    def another_greet():
        name = "Sammy"  # local - this variable only available locally inside another_greet function
        print(f"Hello {name}")  # Hello Sammy

    another_greet()


greet()

# output:
# Hello this is a Global variable String
# Hello Sammy


###########
# Example 4
###########


name = "this is a Global variable String"


def greet():
    name = "Adam"  # enclosing variable
    print(f"Hello {name}")  # this is a Global variable String

    def another_greet():
        name = "Sammy"  # local - this variable only available locally inside another_greet function
        print(f"Hello {name}")  # Hello Sammy

    another_greet()


greet()

# output:
# Hello Adam
# Hello Sammy


# endregion
