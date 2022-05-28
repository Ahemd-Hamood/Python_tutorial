################################################################
######################## Nested For Loop #######################
################################################################
# region

# nested loop mean add one loop into another loop


for x in range(3):
    for y in range(3):
        print(f'({x}, {y})')

# output:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numbers = [7, 2, 7, 2, 2]

for x in numbers:
    print("x" * x)

# output:
# xxxxxxx
# xx
# xxxxxxx
# xx
# xx

for x in numbers:
    output = ""
    for count in range(x):
        output += 'x'
    print(output)


# output:
# xxxxxxx
# xx
# xxxxxxx
# xx
# xx

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_list = []

for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        my_list.append(x * y)

print(my_list)
# output:
# [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

# endregion
