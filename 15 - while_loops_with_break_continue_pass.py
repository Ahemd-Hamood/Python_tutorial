################################################################
######################## While Loop ############################
################################################################
# region

# while loop is used to execute a block of code multiple times when the condition is true, the execution stops when our condition chang to false.
# We write a while statement then after that we specify our boolean condition, after the boolean condition we add a colon ':'
# If your while loop is true, and always set to True, this will cause an infinite loop, so we must change our condition to False in some point on the way.

# Syntax:

# while your_condition:
# block of code run when our condition is True
# .............
# .............

# >> The following cause an infinite Loop :-
# while True:
#   print("Running......")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >> In the following example, we loop thru i from 1 to 5, every time we enter the loop i value is incremented by +1, till the while condition becomes False

i = 1

while i <= 5:
    print(i)
    i += 1  # or i = i + 1

print("Done")

# output:
# 1
# 2
# 3
# 4
# 5
# Done


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - star generating :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

count = 1

while count <= 5:
    print("*" * count)
    count += 1

# output:
# *
# **
# ***
# ****
# *****

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - echo command :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

command = ""

while command.lower() != "quit" and command.lower() != 'exit':
    command = input("> ")
    print("Echo", command)

# output:
# > command 1
# Echo command 1
# > command 2
# Echo command 2
# > command 3
# Echo command 3
# > quit || exit
# Echo quit

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example  :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

counter = 0

while counter <= 5:
    print(f'counter: {counter}')
    counter += 1  # increase counter by +1 - counter = counter + 1
else:
    print("counter Done")

print("Next Code")

# Output:
# counter: 0
# counter: 1
# counter: 2
# counter: 3
# counter: 4
# counter: 5
# counter Done
# Next Code

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example  :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = 50

while x > 1:
    print(f"current value of x is {x}")
    x -= 5
else:
    print("this is the end")

# current value of x is 50
# current value of x is 45
# current value of x is 40
# current value of x is 35
# current value of x is 30
# current value of x is 25
# current value of x is 20
# current value of x is 15
# current value of x is 10
# current value of x is 5
# this is the end


# endregion

################################################################
##############  Using break, continue and pass  ################
################################################################
# region
print("-----------------------------------------------------------------------------------")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 1 - using break statement to break the entire loop :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_counter = 0

while my_counter <= 10:
    print(f"current count is {my_counter}")
    if my_counter == 5:
        break
    my_counter += 1
else:
    print("stops at 5")

# Output:
# current count is 0
# current count is 1
# current count is 2
# current count is 3
# current count is 4
# current count is 5

print("-----------------------------------------------------------------------------------")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 2 - using continue statement to jump at the beginning of the loop :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_counter = 0

while my_counter <= 10:
    my_counter += 1
    if my_counter == 5:
        continue
    print(f"current count is {my_counter}")
else:
    print("stopped")

# Output:
# current count is 1
# current count is 2
# current count is 3
# current count is 4
# current count is 6
# current count is 7
# current count is 8
# current count is 9
# current count is 10
# current count is 11
# stopped

print("-----------------------------------------------------------------------------------")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 3
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = 0

while x < 5:
    if x == 2:
        break
    print(f"x = {x}")
    x += 1

# Output:-
# x = 0
# x = 1

print("-----------------------------------------------------------------------------------")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 4 - using pass statement to do nothing :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_counter = 0

while my_counter <= 10:
    my_counter += 1
    if my_counter == 5:
        continue
    print(f"current count is {my_counter}")
else:
    print("stopped")

# output:
# current count is 1
# current count is 2
# current count is 3
# current count is 4
# current count is 6
# current count is 7
# current count is 8
# current count is 9
# current count is 10
# current count is 11
# stopped

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 5 - echo command with break keyword :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

while True:
    command = input(">")
    print("Echo", command)
    if command.lower() == "quit":
        break

# output:
# > command 1
# Echo command 1
# > command 2
# Echo command 2
# > command 3
# Echo command 3
# > quit
# Echo quit


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 6 - We use the pass keyword to leave our loops code block empty :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = [1, 2, 3, 4, 5]

while False:
    pass

for item in x:
    pass


# endregion

################################################################
#######################  Example 1 #############################
################################################################
# region

secret_number = 9
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess_number = int(input("Your Guess= "))
    guess_count += 1
    if guess_number == secret_number:
        print("You Win !")
        break
else:
    print("Sorry Try again")

# output 1:
# Your Guess= 1
# Your Guess= 2
# Your Guess= 3
# Sorry Try again

# output 2:
# Your Guess= 1
# Your Guess= 3
# Your Guess= 9
# You Win !

# endregion
