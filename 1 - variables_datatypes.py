# ####################################
# 0. what is variable datatype ?
# ####################################
# region
# We use variable to temporary store data in computer memory
# variable is a name that is used to identify and hold value, also it's used to refer to memory location
# our variable has a datatype or variable type. In python we don't specify the type of variable because
# python can figure out the datatype by itself.
# values in python are called objects

# endregion

# ####################################
# 1. >> Variable Syntax :-
# ####################################
# region

# <variable name> = variable_value: number, string, boolean, list, tuples, dictionary, etc...

# when creating a variable name by convention we write a variable with small case and separate word with underscore
from re import X


username = "Fox345"
data_of_birth = "12/3/90"

# endregion

# ####################################
# 2. >> Variable value datatypes  :-
# ####################################
# region

string_variable = "string"
number_integer_variable = 123
number_float_variable = 12.55
boolean_variable = True
boolean_variable = False
list_variable = [1, 2, 3, 4, "5"]
dictionary_variable = {
    "name": "Adam",
    "age": 34,
    "price": 2.44
}
tuple_variable = ("one", 2, "three", 3.0)
set_variable = set("1")

# A - Numeric, sequence and boolean Datatypes :-
# 1. Integers (int) -> the value of a whole number like 1, 345, 243345
# 2. Floating point (float) -> the value of a decimal number like 2.3, 4.6, 100.0
# 3. Strings (str) -> the value of an ordered sequence of characters like "Adam", 'Dog', "2012"
# 4. Booleans (bool) -> it hold a logical value like True or False

# B - Data structure Datatypes which hold different datatype values :-
# 1. Lists (list) -> it holds an ordered sequence of objects similar to array - for example [10 , 'adam', 99.99]
# 2. Dictionaries (dict) -> it holds un-ordered { key:value } pair - for example { "Key": "Value", "Name": "Adam", "TicketNo": 23 }
# 3. Tuples (tup) -> its an ordered immutable (can't change) sequence of objects - for example ( "adam", 34, 22.35 )
# 4. Sets (set) -> its un-ordered collection of unique objects - for example { "a", "b" }

# endregion

# ####################################
# 3. >> Rules when writing variables names  :-
# ####################################
# region

# 1. variables can not start with number -> 12Name = #, 1234 = #
# 2. variable naming can not contain spaces, instead you can use underscore -> full Name = ## (wrong) -- full_Name = # (correct) -- _username = # (correct)
# 3. you can use the following symbols on your variable names --> :'",<>/?|\!@#%^&*~-+
# 4. we have reserved keyword in python like 'list' and 'str'
# 5. python popular for lowercase naming --> name, username, title_stamp

# endregion

# ####################################
# 4. >> Create Variables :-
# ####################################
# region

# A - Create a variable called name and assign to it a value of type string
name = "Adam William"
print("Your Name: " + name)  # output: Your Name: Adam William

# B - Create a variable called price of type number-integer and assign to it a value of type number-integer
price = 120
print("Your Balance is: ")  # output: Your Balance is:
print(price)  # output: 120

# C - Create variable name with a value of type float number
rating = 4.6
print("The Rate is ")  # output: The Rate is:
print(price)  # output: 4.6

# D - Create variable name with a value of type Boolean
is_published = True
print("The Book is Published: ")  # output: The Book is Published:
print(is_published)  # output: True

# endregion

# ####################################
# 5. >> Create multiple Variables with same value assignment :-
# ####################################
# region

var_1, var_2, var_3 = 100, 200, 300 # --> var_1, var_2, var_3 = (100, 200, 300)

print(var_1)  # output: 100
print(var_2)  # output: 100
print(var_3)  # output: 100

# endregion

# ####################################
# 6. >> Re-assign ot Update variables :-
# ####################################
# region

# We can re-assign or update the value of our existed variable, just by declare the variable again

# A - Create a variable and assign value to it, then update it's value again
price = 120
print(price)  # output: 120
price = 699
print(price)  # output: 699

# B - Another Example
name = "Adam"
print(name)  # output: Adam
price = "Frank"
print(name)  # output: Frank

# endregion

# ####################################
# 7. >> Create More variables with different value datatype :-
# ####################################
# region

price = 10  # integer number datatype value
rating = 4.9  # float number datatype value
name = "Adam"  # string datatype value
is_published = True  # boolean datatype value
is_admin = False  # boolean datatype value
# and other complex datatype later......

# endregion

# ####################################
# 8. >> Swapping Variables
# ####################################
# region

x = 10
y = 20

z = x
x = y
y = z

print(x)  # output: 20
print(y)  # output: 10

# >> We can simply swipe variables without creating a third variable, with tuple defining but without parenthesis 

x = 10
y = 20

x, y = y, x  # --> x,y = (20, 10)

print(x)  # output: 20
print(y)  # output: 10

# endregion

# ####################################
# 9. >> An Example of creating variables
# ####################################
# region

# In hospital we have to check a patient name John Smith he is 20 years old and is a new patient

patient_name = "John Smith"
patient_age = 20
is_patient_new = True

# endregion
