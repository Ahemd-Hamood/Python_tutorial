################################################################
# Using Ternary operators to shorten if-else condition statement
################################################################
# region

# Ternary operators are conditional expressions that evaluate condition based on being True oe False

# >> Syntax:
# value_if_true if condition else value_if_false

age = 22
message = ""

if age > 18:
    message = "Accepted"
else:
    message = "Not Accepted"

print(message)
# output: Accepted

# >> you can shorten the conditional statement above using ternary expression as following :-

message = "Accept" if age > 18 else "Not Accepted"

print(message)
# output: Accepted

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

is_nice = False

current_status = "Happy" if is_nice else "Not happy"
print(current_status)
# output: Not happy

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

condition = True

my_number = 3 if condition else 44
print(my_number)
# output: 3

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

username = ""

access = f"Welcome {username}" if username else "Empty Username"
print(access)
# output: Empty Username

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

quantity = 0

msg = f"We have {quantity} Items" if quantity else "nothing is available"
print(msg)
# output: nothing is available

quantity = 14

msg = f"We have {quantity} Items" if quantity else "nothing is available"
print(msg)
# output: We have 14 Items

# endregion


################################################################
# Using Ternary operators with 'or' operator
################################################################
# region
print("#" * 50)

print(True or False)  # output: True
print(True or "")  # output: True
print("" or True)  # output: True

print("ABC" or True)  # output: ABC
print(True or "ABC")  # output: True
print(False or "text")  # output: text

print([] or "text")  # output: text
print({} or "text")  # output: text
print(0 or "text")  # output: text

# >>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>

input = None
msg = input or "No Data"
print(msg)  # No Data

# endregion
