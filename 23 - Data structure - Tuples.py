################################################################
######################## Define Tuples #########################
################################################################
# region

# Tuples is a read only list that contain a sequence of objects, but we can't modify this sequence, we can say that tuple is immutable.
# like adding a new objects to it,, and also we can't remove an existing object and also we can't modify an existing object.

# To define tuples we use open-close parentheses () or without parentheses but you must add a trailing comma , then we add our objects like numbers, strings, boolean, lists, tuples, etc....
# like the following :-

mix_tuples = ("a", 2, True, 32.4, [3, 4, 3], (1, 2, 3))
mix_tuples = "a", 2, True, 32.4, [3, 4, 3], (1, 2, 3)

print(type(mix_tuples))
# output:
# <class 'tuple'>

print(mix_tuples)
# output:
# ('a', 2, True, 32.4, [3, 4, 3], (1, 2, 3))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. >> If you are planing to have a single item inside your tuples with no parentheses, you must add a trailing comma at the end
# just to tell python interpreter that you are defining a tuples instead of an integer
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
single_item_tuple = 1,

print(type(single_item_tuple))
# output:
# <class 'tuple'>

print(single_item_tuple)
# output:
# (1,)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# B. >> Define an empty tuple ()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

empty_tuple = ()
print(type(empty_tuple))
# output:
# <class 'tuple'>

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# C. >> Concatenate/repeat tuples :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

concat_tuples = (1, 2, 3) + (4, 5, 6)

print(type(concat_tuples))
# output:
# <class 'tuple'>

print(concat_tuples)
# output:
# (1, 2, 3, 4, 5, 6)

repeat_tuples = (1, 2) * 3

print(repeat_tuples)
# output:
# (1, 2, 1, 2, 1, 2)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# D. >> Tuple is immutable can't be changed
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_tuple = (1, 2, 3, 4, 5)

# my_tuple[0] = 2
# output:
# TypeError: 'tuple' object does not support item assignment

# endregion

################################################################
######### Convert iterable List/String into tuples #############
################################################################
# region

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. >> Convert list into tuples
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
my_list = [1, 2, 3]

to_tuple = tuple(my_list)

print(to_tuple)
# output:
# (1, 2, 3)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# B. >> Convert String into tuples
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_string = "Hello"

to_tuple = tuple(my_string)

print(to_tuple)
# output:
# ('H', 'e', 'l', 'l', 'o')

# endregion

################################################################
##################### Access Tuples [0], [:] ###################
################################################################
# region

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. >> Access and return single Item
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[0])  # output: 1
print(my_tuple[1])  # output: 2
print(my_tuple[4])  # output: 5

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. >> Access and return range of Items [:]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers[0:])  # output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[2:])  # output: (3, 4, 5, 6, 7, 8, 9)
print(numbers[5:])  # output: (6, 7, 8, 9)
print(numbers[-1:])  # output: (9,)
print(numbers[-4:])  # output: (6, 7, 8, 9)
print(numbers[-7:])  # output: (3, 4, 5, 6, 7, 8, 9

print("----------------------------------")

print(numbers[:0])  # output: ()
print(numbers[:3])  # output: (1, 2, 3)
print(numbers[:7])  # output: (1, 2, 3, 4, 5, 6, 7)
print(numbers[:-1])  # output: (1, 2, 3, 4, 5, 6, 7, 8)
print(numbers[:-3])  # output: (1, 2, 3, 4, 5, 6)
print(numbers[:-6])  # output: (1, 2, 3)

print("----------------------------------")

print(numbers[0:1])  # output: (1)
print(numbers[0:5])  # output: (1, 2, 3, 4, 5)
print(numbers[1:6])  # output: (2, 3, 4, 5, 6)
print(numbers[4:8])  # output: (5, 6, 7, 8)
print(numbers[1:-2])  # output: (2, 3, 4, 5, 6, 7)
print(numbers[3:-2])  # output: (4, 5, 6, 7)
# output: () starting with negative number always will return () empty tuple
print(numbers[-1:-2])

# endregion

################################################################
######################## Use in operator #######################
################################################################
# region

my_tuple = (1, 2, 3)

if 2 in my_tuple:
    print("exists")

print(3 in my_tuple)  # output: True
print(4 in my_tuple)  # output: False


# endregion

################################################################
######################## Tuples variable Unpacking #############
################################################################
# region

coordinates = (1,2,3)

x,y,z = coordinates

print(x) # output: 1
print(y) # output: 2
print(z) # output: 3

# endregion