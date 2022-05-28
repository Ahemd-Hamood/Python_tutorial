################################################################
######################## For Loop ##############################
################################################################
# region

# for loop is used to iterate over items of collection, such as string, list, etc...
# string is a sequence of characters, so it consider as a collection.

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> Example - Iterate ove string
# >>>>>>>>>>>>>>>>>>>>>>>>

my_string = "abcdef"

for item in my_string:
    print(item)

# >> Out Item will hold a single character on each iteration.
# output:
# a
# b
# c
# d
# e
# f

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> Example - Iterate ove string of numbers
# >>>>>>>>>>>>>>>>>>>>>>>>

my_nums = "12345"

for item in my_nums:
    print(item)

# output:
# 1
# 2
# 3
# 4
# 5

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> Example - Iterate thru list of numbers
# >>>>>>>>>>>>>>>>>>>>>>>>

my_nums = [1, 2, 3, 4, 5]

for item in my_nums:
    print(item)

# output:
# 1
# 2
# 3
# 4
# 5

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> Example - Iterate thru list of names
# >>>>>>>>>>>>>>>>>>>>>>>>

my_names = ["Adam", "Sara", "John", "Kim"]

for item in my_names:
    print(item)

# output:
# Adam
# Sara
# John
# Kim

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> Example - Using the range() function, from 0 to 5
# >>>>>>>>>>>>>>>>>>>>>>>>

for item in range(0, 6):
    print(item)

# output:
# 0
# 1
# 2
# 3
# 4
# 5

print(list(range(6)))
# output: [0, 1, 2, 3, 4, 5]

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> Example - Using the range() function, from 5 to 10
# >>>>>>>>>>>>>>>>>>>>>>>>

for item in range(5, 11):
    print(item)

# output:
# 5
# 6
# 7
# 8
# 9
# 10

print(list(range(5, 11)))
# output: [5, 6, 7, 8, 9, 10]

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> Example - Using the range() function, from 0 to 10 of 2 steps
# >>>>>>>>>>>>>>>>>>>>>>>>

for item in range(0, 11, 2):
    print(item)

# output:
# 0
# 2
# 4
# 6
# 8
# 10

print(list(range(0, 11, 2)))
# output: [0, 2, 4, 6, 8, 10]

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> Example
# >>>>>>>>>>>>>>>>>>>>>>>>

for number in range(1, 4):
    print("Attempt", number, number * ".")

# output:
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...

print(list(range(1, 4)))
# output: [1, 2, 3]

# endregion

################################################################
######################## For-else with break ################### 
################################################################
# region

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
status = True

for number in range(3):
    print("Attempt")
    if status:
        print("OK")
else:
    print("Failed")

# output:
# Attempt
# OK
# Failed

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
status = True

for number in range(3):
    print("Attempt")
    if status:
        print("OK")
        break

# output:
# Attempt
# OK

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# break will exist the for loop including the else block
status = True

for number in range(3):
    print("Attempt")
    if status:
        print("OK")
        break
else:
    print("Failed")

# output:
# Attempt
# OK

# endregion

################################################################
########################### Example ############################
################################################################
# region
print("#" * 50)

prices = [10, 20, 30]
total = 0

for item in prices:
    total += item

print(f"total price is {total}")
# output: total price is 60


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - print the even numbers
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

count = 0

for number in range(1, 10):
  if number % 2 == 0:
    count += 1
    print("Even: ", number)

print(f"We have {count} even numbers")

# output:
# Even:  2
# Even:  4
# Even:  6
# Even:  8
# We have 4 even numbers

# endregion
