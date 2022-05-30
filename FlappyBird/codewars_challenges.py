# define a function to convert PascalCase to snake_case
def to_snake_case(name):
    if isinstance(name, int): return str(name)
    # define a list to store the snake_case
    snake_case = []
    # define a variable to store the length of the name
    length = len(name)
    # define a variable to store the index
    index = 0
    # loop through the name
    while index < length:
        # check if the current character is uppercase
        if name[index].isupper():
            # if it is uppercase, add a '_' and the lowercase version of the character to the snake_case list
            snake_case.append('_')
            snake_case.append(name[index].lower())
        # otherwise, add the character to the snake_case list
        else:
            snake_case.append(name[index])
        # increment the index
        index += 1
    # join the snake_case list into a string
    return ''.join(snake_case)

def to_underscore(string):
    return ''.join('_'+c.lower() if c.isupper() else c for c in str(string)).lstrip('_')


#############################################################################################à


# You are given a node that is the beginning of a linked list. 
# This list always contains a tail and a loop. 
# Your objective is to determine the length of the loop.
def loop_size(node):
    # define a set to store the nodes that have been visited
    visited = list()
    # define a variable to store the current node
    current = node
    # loop through the list
    while current:
        # check if the current node has been visited
        if current in visited:
            # if it has been visited, return the length of the loop
            return len(visited) - visited.index(current)
        # otherwise, add the current node to the visited set
        visited.append(current)
        # set the current node to the next node
        current = current.next
    # if the loop has ended, return 0
    return 0

def loop(node):
    turtle, rabbit = node.next, node.next.next
    
    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count


################################################################################################################


# Given a list of integers and a single sum value, 
# return the first two values (parse from the left please) in order of appearance that add up to form the sum.
def sum_pairs(ints, s):
    # define a set to store the numbers that have been visited
    visited = set()
    # loop through the list
    for num in ints:
        # check if the current number has been visited
        if s - num in visited:
            # if it has been visited, return the numbers
            return [s - num, num]
        # otherwise, add the current number to the visited set
        visited.add(num)
    # if the loop has ended, return None
    return None


############################################################################################################


# return who is the "survivor", ie: the last element of a Josephus permutation.
def josephus_survivor(n, k):
    # define a list to store the numbers
    nums = list(range(1, n+1))
    # define a variable to store the index
    index = 0
    # loop through the list
    while len(nums) > 1:
        # set the index to the next index
        index = (index + k - 1) % len(nums)
        # remove the element at the index
        nums.pop(index)
    # return the last element
    return nums[0]

def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1): v = (v + k) % i
    return v + 1


############################################################################################################

