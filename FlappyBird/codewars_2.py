# define the function scramble(str1, str2) 
# that returns true if a portion of str1 characters can be rearranged to match str2, 
# otherwise returns false.
def scramble(s1, s2):
    for i in s2:
        if i not in s1:
            return False
    return True

def scramble(s1, s2):
    return set(s2).issubset(set(s1))

def scramble(s1, s2):   # letsgooooooo
    if all([s2.count(c) <= s1.count(c) for c in set(s2)]):
        return set(s2).issubset(set(s1))
    return False


################################################################################################

# define a function that takes a list of integers and returns
# a string with each number separated by a comma and dashes '-' between adjacent numbers
# e.g. [1, 2, 3, 4, 5] -> '1-5'
# e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> '1-10'
def dash_insert(numbers):
    return '-'.join(str(numbers[i]) + str(numbers[i+1])[0] for i in range(len(numbers)-1))

def solution(l):
    return ','.join(
        ['-'.join(
            map(str, range(i, j + 1))) if j - i >= 2 
            else str(i) for i, j in zip(l, l[1:])])
         
def detect_range(input_list):
    start = None
    length = 0

    for elem in input_list:

        # First element
        if start is None:
            start = elem
            length = 1
            continue

        # Element in row, just count up
        if elem == start + length:
            length += 1
            continue

        # Otherwise, yield
        if length == 1:
            yield start
        else:
            yield (start, start+length)

        start = elem
        length = 1

    if length == 1:
        yield start
    else:
        yield (start, start+length)

a = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(list(detect_range(a)))
def solution(l):
    ranges = list(detect_range(l))
    print(ranges)
    sol = ''
    for e in ranges:
        if isinstance(e, int): sol += str(e) + ','
        elif e[0] == e[1] - 2:
            sol += str(e[0]) + ',' + str(e[0]+1) + ','
        else:
            sol += str(e[0]) +'-'+str(e[1]-1)+','
            
    return sol.rstrip(',')

# a well made one
def solution(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b+1:
            ranges.append(str(a) if a == b else "{}{}{}".format(a, "," if a+1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)


######################################################################################

# The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.
# But some of the rats are deaf and are going the wrong way!
# How many deaf rats are there?
# Legend
# P = The Pied Piper
# O~ = Rat going left
# ~O = Rat going right
# Example
# ex1 ~O~O~O~O P has 0 deaf rats
# ex2 P O~ O~ ~O O~ has 1 deaf rat
# ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats
# write a function to count O~ before P and ~O after P
def deaf_rats(n):
    return n.count('~O') - n.count('O~') 
    