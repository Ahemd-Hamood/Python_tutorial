################################################################
# Arithmetic operations
################################################################
# region

integer_number = 23  # whole number
float_number = 2.56  # floating number with decimal points

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Some mathematic operations with = +,-,*,/,% operators
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print(10 + 4)  # output: 14
print(10 - 6)  # output: 4
print(12 / 6)  # output: 2.0
print(10 / 3)  # output: 3.3333333333333335
print(10 // 3)  # output: 3
print(2 * 6)  # output: 12

print(2 % 6)  # output: 2 -> 6 X 0 = 0 remaining 2 to reach 6
print(2 % 12)  # output: 2 -> 12 X 0 = 0 remaining 2 to reach 12

print(10 % 3)  # output: 2 -> 3 X 3 = 9 remaining 1 to reach 10
print(7 % 4)  # output: 3 -> 4 X 1 = 4 remaining 3 to reach 7
print(50 % 5)  # output: 0 -> 5 X 10 = 50 remaining 0 to reach 50
print(23 % 2)  # output: 1 -> 2 X 11 = 22 remaining 1 to reach 23
print(22 % 2)  # output: 0 -> 2 X 11 = 22 remaining 0 to reach 22

print("*" * 40)

print(2 ** 3)
# output: 8 -> 2 x 2 x 2 = 8
print(10 ** 3)
# output: 10 -> 10 x 10 x 10 = 1000

# endregion

################################################################
# Precedence Operator
################################################################
# region

# Precedence Operator order - top-bottom = higher-lower:-
# 1. Exponentiation '**' -> 2 ** 2
# 2. Multiplication '*' -> 2 * 2
# 3. Division '/' -> 2 / 2
# 4. Addition '+' -> 2 + 2
# 5. Subtraction '-' -> 2 - 2

print(10 + 3 * 2)
# output: 16
# 10 + (3 * 2)
# 10 + 6
# 16

print(2 + 10 * 10 + 3)
# output: 105
#  2 + (10 * 10) + 3
# 2 + 100 + 3
# 105


print(10 - 4 * 10 + 3 + 7)
# output: -20
# 10 - (4 * 10) + 3 + 7
# 10 - 40 + (3 + 7)
# (10 - 40) + 10
# -30 + 10
# -20

print(10 + 3 * 2 ** 2)
# output: 22
# 10 + 3 * (2 ** 2)
# 10 + (3 * 4)
# 10 + 12
# 22

# Using parenthesis to change order to be executed first :-

print((2 + 10) * (10 + 3))
# output: 156
# (2 + 10) * (10 + 3)
# 12 * 13
# 156

print((2 + 3) * 10 - 3)
# output: 47
# (2 + 3) * 10 - 3
# 5 * 10 - 3
# (5 * 10) - 3
# 50 - 3
# 47

# endregion

################################################################
# Increment and Decrement Numbers
################################################################
# region
x = 10
x = x + 1
# OR
x += 1

x = 20
x += 5
print(x)  # output: 25
x -= 5
print(x)  # output: 20
x *= 2
print(x)  # output: 40

# endregion
