from sys import getsizeof

values = [x * 2 for x in range(5)]

for x in values:
    print(x)

# output:
# 0
# 2
# 4
# 6
# 8

# In the example above, imaging having range(100,000) items which is a really large dataset or infinite stream of data
# all items that we are storing inside a list are actually stored in memory,
# if we have a list with 100,000 Items then you should not store those value in the memory because that's very memory inefficient

# >> Having the following will be too much for the memory, 10000 items inside our list :-

values = [x * 2 for x in range(10000)]

# Here we have to use a generator object, generator object are iterable just like list, but in generator on each iterate it generates a new number value output.
# Unlike list it provide all items value in advance and store all value in memory, that why we use generator list to save memory and generate items on demand.

# values = [x * 2 for x in range(10000)]  # normal list - inefficient way
# output:
# [......] 0 - 10000

values = (x * 2 for x in range(10000))  # generator object - efficient way
print(values)
# output:
# 0
# 2
# 4
# 6
# 8
# <generator object <genexpr> at 0x00000129BFEE9A10>

# lets compare the size of generator object vs list with 10000 items
# We will import the getsizeof() function from sys module/library

values = [x * 2 for x in range(10000)]
print(getsizeof(values))
# output:
# 85176

values = (x * 2 for x in range(10000)) 
print(getsizeof(values))
# output:
# 104

values = (x * 2 for x in range(1000000)) 
print(getsizeof(values))
# output:
# 104

# As you see using generator object is more efficient and don't take up much memory,If we use list we would end up with a list of 100,000 or 1,000,000 items

#################################################
# In situations where you're dealing with a large dataset or an infinite stream of data, you better use a "generator expression object" ().
# When we use parentheses around the comprehension expression, just be a ware that generator object don't store all the items in memory, 
# for that you won't get the total number of items you're working with, but you will get an error "object of type 'generator' has no len()"
#################################################


values = [x * 2 for x in range(10000)]
print(len(values))
# output:
# 10000

values = (x * 2 for x in range(10000)) 
print(len(values))
# output:
# TypeError: object of type 'generator' has no len()
