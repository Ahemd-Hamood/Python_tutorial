################################################################
####### Define Dictionary - Access/Update/Add/delete/clear() ###
################################################################
# region

# Dictionary is a collection of key-value pairs, which is used to map a key to value.
# We define dictionary by opening curly bracelet {}, and adding "key": "value", and we assign value to key using ":" colon
# We wrap Keys around double quotes "", and value string with "" and numbers, list, tuples without double quotes :
# String Value -> "name": "Adam"
# Number Value -> "age": 123
# list Value -> "items": [1, "apple", "banana"]
# tuple Value -> "tuples": (2,6,7,8),
# set Value ->  "sets": {1, 2, 3, 4, 5, 6, 7}
# Each key-value pair is separated by comma ',' -> { "key1": "value", "key1": "value", .... }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. >> Defining Dictionary :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_dict = {
    "name": "Adam Sam",
    "age": 12,
    "hobbies": ["cook", "swim", "dive"],
    "some_tuples": (2, 6, 7, 8),
    "my_set": {1, 2, 3, 4, 5, 6, 7}
}

print(my_dict)
# output:
# {'name': 'Adam Sam', 'age': 12, 'hobbies': ['cook', 'swim', 'dive'], 'some_tuples': (2, 6, 7, 8), 'my_set': {1, 2, 3, 4, 5, 6, 7}}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# B. >> Using dict() method :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

new_dict = dict(x=1, y=2)
# Similar to:
new_dict = {"x": 1, "y": 2}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# C. >> Access dictionary key-value by specifying the key only :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_dict = {
    "name": "Adam Sam",
    "age": 12,
    "hobbies": ["cook", "swim", "dive"],
    "some_tuples": (2, 6, 7, 8),
    "my_set": {1, 2, 3, 4, 5, 6, 7}
}

print(my_dict["name"])
# output: Adam Sam
print(my_dict["age"])
# output: 12
print(my_dict["some_tuples"])
# output: (2, 6, 7, 8)
print(my_dict["hobbies"])
# output: ['cook', 'swim', 'dive']

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# D. >> Update dictionary :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_dict = {
    "name": "Adam Sam",
    "age": 12,
    "hobbies": ["cook", "swim", "dive"],
    "some_tuples": (2, 6, 7, 8),
    "my_set": {1, 2, 3, 4, 5, 6, 7}
}

my_dict["name"] = "William David"

print(my_dict["name"])
# output:
# William David

my_dict["age"] = 23
my_dict["hobbies"].append("hiking")
my_dict["name"] = ""

print(my_dict)
# output:
# { 'name': '',
#   'age': 23,
#   'hobbies': ['cook', 'swim', 'dive', 'hiking'],
#   'some_tuples': (2, 6, 7, 8),
#   'my_set': {1, 2, 3, 4, 5, 6, 7}
# }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# E. >> Add new Key-value into an existing dictionary:-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

some_dict = {
    "name": "Sally"
}

some_dict["age"] = 34
some_dict["price"] = 3.88
some_dict["hobbies"] = ['cook', 'swim', 'dive', 'hiking']

print(some_dict)
# output:
# {
#  'name': 'Sally',
#  'age': 34,
#  'price': 3.88,
#  'hobbies': ['cook', 'swim', 'dive', 'hiking']
# }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# E. >> Use del keyword to delete a key Item
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_dict = {
    "name": "Adam Sam",
    "age": 12,
    "hobbies": ["cook", "swim", "dive"],
    "some_tuples": (2, 6, 7, 8),
    "my_set": {1, 2, 3, 4, 5, 6, 7}
}

del my_dict["my_set"]
del my_dict["hobbies"]

print(my_dict)
# output:
# {
#   'name': 'Adam Sam',
#   'age': 12,
#   'some_tuples': (2, 6, 7, 8)
# }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# F. >> Use clear() method to delete all keys and their value from the dictionary
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_dict = {
    "name": "Adam Sam",
    "age": 12,
    "hobbies": ["cook", "swim", "dive"],
    "some_tuples": (2, 6, 7, 8),
    "my_set": {1, 2, 3, 4, 5, 6, 7}
}

print(my_dict)
# output:
# {'name': 'Adam Sam', 'age': 12, 'hobbies': ['cook', 'swim', 'dive'], 'some_tuples': (2, 6, 7, 8), 'my_set': {1, 2, 3, 4, 5, 6, 7}}

my_dict.clear()
print(my_dict)
# output:
# {}

# endregion

################################################################
## Use the get() method to retrieve key-value without an error #
################################################################
# region

some_dict = {
    "name": "Sally"
}

# print(some_dict["age"])
# output:
# KeyError: 'age'

# if we use the get() method to retrieve non-existed Key, it will return None instead of returning an error

print(some_dict.get("name"))  # output: Sally
print(some_dict.get("age"))  # output: None

# You can provide a default value, if key does not exist

print(some_dict.get("age", 0))  # output: 0
print(some_dict.get("company", "Anonymous"))  # output: Anonymous
print(some_dict.get("name", "Unknown"))  # output: Sally

# endregion

################################################################
########## Use 'in' operator to check Key existence ##############
################################################################
# region

points = {
    "x": 1,
    "y": 2
}

if "x" in points:
    print("Key does exist")

# output:
# Key does exist

if "z" in points:
    print("Key does exist")
else:
    print("Key does not exist")

# output:
# Key does not exist

print("x" in points)  # output: True
print("y" in points)  # output: True
print("z" in points)  # output: False

# endregion

################################################################
################# Loop over a dictionary #######################
################################################################
# region

my_dict = {
    "name": "Adam Sam",
    "age": 12,
    "hobbies": ["cook", "swim", "dive"],
    "some_tuples": (2, 6, 7, 8),
    "my_set": {1, 2, 3, 4, 5, 6, 7}
}

# >> Here we loop over keys only

for key in my_dict:
    print(key)

# output:
# name
# age
# hobbies
# some_tuples
# my_set

for key in my_dict:
    print(f"{key}: {my_dict[key]}")

# output:
# name: Adam Sam
# age: 12
# hobbies: ['cook', 'swim', 'dive']
# some_tuples: (2, 6, 7, 8)
# my_set: {1, 2, 3, 4, 5, 6, 7}

# >> Using items() method to return a tuple :-

for tup in my_dict.items():
    print(tup)

# output:
# ('name', 'Adam Sam')
# ('age', 12)
# ('hobbies', ['cook', 'swim', 'dive'])
# ('some_tuples', (2, 6, 7, 8))
# ('my_set', {1, 2, 3, 4, 5, 6, 7})

for key, val in my_dict.items():
    print(f"{key}: {val}")

# output:
# name: Adam Sam
# age: 12
# hobbies: ['cook', 'swim', 'dive']
# some_tuples: (2, 6, 7, 8)
# my_set: {1, 2, 3, 4, 5, 6, 7}


# endregion

################################################################
################### Dictionary Comprehensions ##################
################################################################
# region

values = {x: x*2 for x in range(5)}

print(values)
# output:
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# endregion
