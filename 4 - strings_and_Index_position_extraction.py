# ####################################
# 1. String with single/double quotes
# ####################################
# region

# As we know we define our strings between single or double quotes, the single quotes is used most so we are going to use it, as you wish
# but be aware in some cases we are going to use double quotes when we have a single quote indie our string, like this "we're going to the park"

title = 'this is string in python'
print(title)
# output: this is string in python
# -----------------------------------------
# msg = 'We're going' # here our string start with W and end with e, we better use double quotes in this case
# -----------------------------------------
# Placing a single quotes inside a double quotes string
msg = "We're going to the park"
print(msg)  # output: We're going to the park
# -----------------------------------------
# Placing double quotes inside a single quotes string
msg = 'define "something" in your way'
print(msg)  # output: define "something" in your way
# -----------------------------------------
# full_text = '
#  We can't have multiple line string, so we are going to use triple quotes string next
# '


# endregion

# ####################################
# 2. String with Triple quotes
# ####################################
# region

# The Triple quotes sting allow us to have a span of strings/text on multiple lines

message = '''
  MultiLine string ...
  Line 1 - some text here
  Line 2 - some text here
  Line 3 - some text here
'''

print(message)
# output:
# MultiLine string ...
# Line 1 - some text here
# Line 2 - some text here
# Line 3 - some text here

# >> Another Example

email_message = '''
Dear John,

We are really sorry to inform you .......

Thank you, 
The support Team
'''

print(email_message)
# Dear John,

# We are really sorry to inform you .......

# Thank you,
# The support Team

# endregion

# ####################################
# 3. String Escape Sequence
# ####################################
# region

# \" -> to include double quotes inside double quotes string
# \' -> to include single quotes inside single quotes string
# \\ -> to include backslash within a string
# \n -> to print next string in a new line

# >> To include double quotes inside a double quotes string we use backslash escape sequence

my_string = "something \"word\" "
print(my_string)
# output: something "word"

# >> To include single quotes inside a single quotes string we use backslash escape sequence

my_string = 'something \'word\' '
print(my_string)
# output: something 'word'

# >> To include a backslash inside a string

my_string = 'something \\ here '
print(my_string)
# output: something \ here

# >> To include a backslash inside a string

my_string = 'something \nhere '
print(my_string)
# output:
# something
# here

# endregion

# ####################################
# 4. Using Index position to get single character from a string
# ####################################
# region
print("#" * 50)

# The index position always start at 0, you can grab any character from a string,
# just by defining the index position between square brackets your_string[index_position:int]
# "abcdefg"
#  0123456
#  7654321 (with negative sign)
# To get the last character of your string, you can use -1 with negative sign, to start at the end of the string

my_string = "Here we define string"

print(my_string[0])  # output: H - get first index position
print(my_string[2])  # output: r - get second index position
print(my_string[5])  # output: w - get fifth index position
print(my_string[-1])  # output: g - get last index position
print(my_string[-6])  # output: s - from string word

# endregion

# ####################################
# 5. Extract a few string portion
# ####################################
# region

my_string = "abcdefghij"
# The following is similar to print(my_string)
print(my_string[:])
# output: abcdefghij
# ----------  OR  ------------------
print(my_string[::])
# output: abcdefghij

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Define the start index while including it, then print the rest after
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("-" * 50)
# >> Syntax:-
#  mystring[<index_start_and_include_from_here>:]

new_string = "abcdefghij"
#             0123456789
# start from index 0 till the end
print(new_string[0:])
# output: abcdefghij
# ---------------------------------------------
# start from index 5 till the end
print(new_string[5:])
# output: fghij
# ---------------------------------------------
# start from index 7 till the end
print(new_string[7:])
# output: hij
# ---------------------------------------------
# start from start from last index then print after it, which is nothing
print(new_string[-1:])
# output: j

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Define the end start index without including it, then print the rest before
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("-" * 50)
# >> Syntax:-
#  mystring[:<index_start_and_include_from_here>]

new_string = "abcdefghij"

# start from index 0 then print before, which is nothing
print(new_string[:0])
# output: "" - nothing before idex 0
# ---------------------------------------------
# start from index 3 without including it, then print everything before
print(new_string[:3])
# output: abc
# ---------------------------------------------
# start from index 5 without including it, then print everything before
print(new_string[:5])
# output: abcde
# ---------------------------------------------
# start from index 7 without including it, then print everything before
print(new_string[:7])
# output: abcdefg

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Define start and end index - include the start index, and don't include the end index and print in between
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("-" * 50)
# >> Syntax:-
#  mystring[<start_index_include>:<end_index_no_include>]

new_string = "abcdefghij"

# Start at index 0 (include it), and stop at index 3 (don't include) print every thing before it
print(new_string[0:3])
# output: abc
# ---------------------------------------------
# Start at index 3 (include it), and stop at index 7 (don't include) print every thing before it
print(new_string[3:7])
# output: defg
# ---------------------------------------------
# Start at index 3 (include it), and stop at index 7 (don't include) print every thing before it
print(new_string[5:8])
# output: fgh
# ---------------------------------------------
# Start at index 1 (include it), and stop at index -1 (don't include) print every thing before it
print(new_string[1:-1])
# output: bcdefghi
# ---------------------------------------------
# Start at index 2 (include it), and stop at index -4 (don't include) print every thing before it
print(new_string[2:-4])
# output: cdef

# endregion
