################################################################
############# Define Sets - Add/Remove/len() ###################
################################################################
# region

# Sets is un-order collection of objects/item with no duplicates, each item inside our collection is unique.
# Sets are un-ordered collections, so you can not access an individual item
# If we have a list of numbers with duplicate numbers, you can remove these duplicate number by converting the list into set
# We use curly braces to define sets like this { item1, item2, item3, .... }

# A. >> Define a set

my_set = {1, 2, 3, 4, 5, 6, 7}

print(my_set)
# output:
# {1, 2, 3, 4, 5, 6, 7}

# If you create a new set with duplicate objects/items, our set will remove these duplicate items and keep only one.
my_set = {1, 1, 2, 3, 3, 4, 4, 5}

print(my_set)
# output:
# {1, 2, 3, 4, 5}

# Or

another_set = set()

another_set.add(1)
another_set.add(2)
another_set.add('three')
another_set.add(4)
another_set.add(4) 
another_set.add('five')

print(another_set)
# output: {1, 2, 4, 'three', 'five'}
# Integers comes first, then strings

# B. >> Convert list into set

numbers = [1, 1, 2, 3, 3, 4, 5]
unique_set = set(numbers)

print(unique_set)
# output:
# {1, 2, 3, 4, 5}

# C. >> Add items into our set

set_items = {1, 2}

set_items.add(3)

print(set_items)
# output:
# {1, 2, 3}

set_items.add(4)
set_items.add(5)
set_items.add(6)

print(set_items)
# output:
# {1, 2, 3, 4, 5, 6}

# D. >> Remove an item from the set

set_items = {1, 2, 3, 'a', 'b', 'c'}

set_items.remove('a')
set_items.remove(3)

print(set_items)
# output:
# {1, 2, 'c', 'b'}

# E. >> Get set length

set_items = {1, 2, 3, 'a', 'b', 'c'}

print(len(set_items))
# output:
# 6

# F. >> Can not access individual item

set_items = {1, 2, 3, 'a', 'b', 'c'}

# print(set_items[0])
# TypeError: 'set' object is not subscriptable

# G. >> You add new duplicate and you won't get an error 

my_set = set()

my_set.add(1)
print(my_set)
# output: {1}

my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(5)
print(my_set)
# output: {1, 2, 3, 4, 5}

# >> adding an existing value into set

my_set.add(2)
# No Error Happen, our set will just ignore the value by not adding it into the set
my_set.add(2)
# No Error Happen, our set will just ignore the value by not adding it into the set
my_set.add(2)
# No Error Happen, our set will just ignore the value by not adding it into the set

print(my_set)
# output: {1, 2, 3, 4, 5}

# endregion

################################################################
############ Set Union/Intersection/difference/Symmetric #######
################################################################
# region

# The Unions set_1 | set_2 will include all items that are either in the first set or the second set
# The Unions set_1 & set_2 will return a set that includes all the items that are in both first amd second sets
# The Unions set_1 - set_2 will return a set that get the difference between two sets
# The Unions set_1 ^ set_2 will return the items that are either in the first or second set but not both

numbers = [1, 1, 2, 3, 4]
first_set = set(numbers)

second_set = {1, 5}

result = first_set | second_set

print(result)
# output:
# {1, 2, 3, 4, 5}


result = first_set & second_set

print(result)
# output:
# {1} --> here the only number that exist in both these sets is 1


result = {1, 2, 3, 4, 5} & {1, 2, 3}

print(result)
# output:
# {1, 2, 3}

result = {1, 2, 3, 4, 5} - {1, 2, 3}

print(result)
# output:
# {4, 5} -> {4,5} are not included in the second set

print({1, 1, 2, 3, 4} - {1, 5})
# output:
# {2, 3, 4}


print({1, 1, 2, 3, 4} ^ {1, 5})
# output:
# {2, 3, 4, 5}

print({1, 2, 3, 4, 5} ^ {1, 2, 3})
# output:
# {4, 5}


# endregion

################################################################
############ Using the 'in' operator in Sets ###################
################################################################
# region

my_set = [1, 2, 3, 4, 5]

print(1 in my_set)  # output: True
print(3 in my_set)  # output: True
print(6 in my_set)  # output: False

if 1 in my_set:
    print("Exist")

# output:
# Exist

# endregion

################################################################
################### Set Comprehensions #########################
################################################################
# region

values = { x * 2 for x in range(5) }

print(values)
# output:
# {0, 2, 4, 6, 8}

# endregion