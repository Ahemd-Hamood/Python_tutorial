# ####################################
# 1. Formatted Strings
# ####################################
# region

# string formatting is placing some variables inside your string, instead of concatenate variables with your string like this
# result = "My name is " + name + ", and im from" + nationality
# We can simply use string formatting like the following :-

first_name = "John"
last_name = "Smith"
message = "some messages"

print(first_name + " " + last_name + " with 4 " + message)

# output: John Smith with 4 some messages
# ----------------------------------------------------------------

# >> Using formatted string and place variables between {} as placeholders

print(f"{first_name} {last_name} with 4 {message}")
# output: John Smith with 4 some messages
print(f"Total characters in first_name is {len(first_name)}")
# output: Total characters in first_name is 4
# ----------------------------------------------------------------

# >> Using string format method

print("{0} {1} with 3 {2}".format(first_name, last_name, message))
# output: John Smith with 3 some messages

print("{} {} with 3 {}".format(first_name, last_name, message))
# output: John Smith with 3 some messages

print("{a} {b} with 3 {c}".format(a=first_name, b=last_name, c=message))
# output: John Smith with 3 some messages


# endregion
