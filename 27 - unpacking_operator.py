numbers = [1, 2, 3]

print(numbers)
# output:
# [1, 2, 3]

# to get output like this = 1 2 3 we use the unpacking operator, like this *your_list similar to spread operator in Javascript
# the unpacking operator is used to unpack iterable objects

print(*numbers)
# output:
# 1 2 3

# >>>>>>>>>>>>>>>>>>>>>>>>
# An Example
# >>>>>>>>>>>>>>>>>>>>>>>>

my_list = list(range(5))

print(my_list)
# output:
# [0, 1, 2, 3, 4]

# >> We use the unpacking operator, to unpack range which is iterable

print(*range(5))
# output:
# 0 1 2 3 4

# >> Or we unpack the iterable by taking each individual values, then we put them in a list like the following.

values = [*range(5)]
print(values)
# output:
# [0, 1, 2, 3, 4]

# >> Also we can unpack a string inside a list like this

str_unpack = [*"hello"]
print(str_unpack)
# output:
# ['h', 'e', 'l', 'l', 'o']

# str_unpack = *"hello" // Syntax Error

# >> We can unpack multiple objects inside a list

values = [*range(5), *"hello"]
print(values)
# output:
# [0, 1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o']

# >> Also we can combine multiple lists

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

result = [*list_1, *list_2]
print(result)
# output:
# [1, 2, 3, 4, 5, 6]

# >> Also we can combine multiple lists and add other object

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

result = [*list_1, "-", *list_2, *"bye"]
print(result)
# output:
# [1, 2, 3, '-', 4, 5, 6, 'b', 'y', 'e']

# >> Also we can unpack dictionary

my_dict = {
    "name": "Adam Sam",
    "age": 23,
    "hobbies": ["swim", "hike", "shooting"]
}

other_info = {
    "phone": "123-432-4232",
    "gender": "Male",
    "age": 34
}

combine_dict = {
    *my_dict,
    *other_info
}

print(combine_dict)
# output:
# {'name', 'phone', 'gender', 'hobbies', 'age'}

combine_dict = {
    **my_dict,
    **other_info
}

print(combine_dict)
# output:
# {
#  'name': 'Adam Sam',
#  'age': 34,
#  'hobbies': ['swim', 'hike', 'shooting'],
#  'phone': '123-432-4232',
#  'gender': 'Male'
# }

combine_dict = {
    **my_dict,
    **other_info,
    "status": True
}

print(combine_dict)
# output:
# {
#  'name': 'Adam Sam',
#  'age': 34,
#  'hobbies': ['swim', 'hike', 'shooting'],
#  'phone': '123-432-4232',
#  'gender': 'Male',
#  'status': True
# }
