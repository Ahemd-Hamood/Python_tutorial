from collections import deque

##########################################################################
##########################################################################
############ Default List Stack - LIFO - Last In/First Out  ##############
##########################################################################
##########################################################################
# region

# Stack of items, the last you add is the first that you can remove
# For example stack of books, the last book that you put on top of the stack is the first book that you can remove
# We call it LIFO - Last In/First Out

browser_history = []

# We use the append() method to add an item on top of the stack

browser_history.append("page_1")
browser_history.append("page_2")
browser_history.append("page_3")

print(browser_history)
# output:
# ['page_1', 'page_2', 'page_3']

# We use pop() method to remove last the last item from the stack browser history, when pressing the back button

get_removed_page = browser_history.pop()

print(get_removed_page)
# output:
# page_3

print(browser_history)
# output:
# ['page_1', 'page_2']

# We use stack[-1] to get/return the last/top item from the stack

print("Redirect to:", browser_history[-1])
# output:
# Redirect to: page_2

# check if out browser_history stack is empty, if list == [] then it's falsy which means it's empty :-


def check_stack():
    if not browser_history:
        print("Browser history is empty, disabling back button")
    else:
        print(f"Browser history has {len(browser_history)} items")
        print(f"last Item is {browser_history[-1]}")


check_stack()
# Browser history has 2 items
# last Item is page_2

browser_history.pop()

check_stack()
# Browser history has 1 items
# last Item is page_1

browser_history.pop()

check_stack()
# Browser history is empty, disabling back button

# endregion

##########################################################################
##########################################################################
##### Queues using deque from collection - FIFO - First-In/First-Out #####
##########################################################################
##########################################################################
# region
print("###################### deque ######################")
# To use deque class, we import it from the collection library
# from collections import deque

# To use deque list, we have to pass our empty list as an argument into deque() object
queue = deque([])


# deque object has an append() method which is used to add an item ath the end of the queue list

queue.append("page_1")
queue.append("page_2")
queue.append("page_3")

print(queue)
# output:
# deque(['page_1', 'page_2', 'page_3'])

# We use the popleft() method To remove an item from the beginning of the queue list

queue.popleft()

print(queue)
# output:
# deque(['page_2', 'page_3'])

# check if our queue is empty
def check_queue():
    if not queue:
        print("Browser history is empty, disabling back button")
    else:
        print(queue)
        print(f"Browser history has {len(queue)} items")
        print(f"first Item is {queue[0]}")
        print(f"last Item is {queue[-1]}")

check_queue()
# output:
# deque(['page_2', 'page_3'])
# Browser history has 2 items
# first Item is page_2
# last Item is page_3

queue.popleft()
queue.popleft()

check_queue()
# output:
# Browser history is empty, disabling back button

# endregion
