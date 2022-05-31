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
# print(list(detect_range(a)))
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
import re
def deaf_rats(n):
    p = town.index('P')
    return len(re.findall(r'(?<=O~).*(?=P)', town)) + len(re.findall(r'(?<=P).*(?=~O)', town))

# smart way
def count_deaf_rats(town):
    return town.replace(' ', '')[::2].count('O')

# my solution
import re
def count_deaf_rats(town):
    deaf = 0
    piper = False
    tmp = ''
    for i, v in enumerate(town):
        if v == 'P': piper = True
        elif v == ' ': tmp = ''
        else: tmp += v
        
        if len(tmp) == 2:
            if (not piper and tmp == 'O~') or (piper and tmp == '~O'):
                deaf += 1
            tmp = ''
            
    return deaf


######################################################################################

# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
# N! = 1 * 2 * 3 * ... * N
# Be careful 1000! has 2568 digits
# Good Luck!
def zeros(n):
    return n == 0 and 0 or n//5 + zeros(n//5)

# this does not reach maximum recursion depth
def zeros(n):
    return 0 if n == 0 else n//5 + zeros(n//5)


######################################################################################


# we want to pick the sum of k integers that is closest to the target t
# picking integers from the array ls
# no sorting the list
def choose_best_sum(t, k, ls):
    return min([sum(ls[i:i+k]) for i in range(len(ls)-k+1) if sum(ls[i:i+k]) <= t], key=lambda x: abs(x-t))

# actually this is the best solution
def choose_best(t,k,ls):
    if k == 0: return 0
    best = -1
    for i, v in enumerate(ls):
        if v > t: continue
        b = choose_best(t - v, k - 1, ls[i+1:])
        if b < 0: continue
        b += v
        if b > best and b <= t:
            best = b
    return best

def choose_best_sum(t, k, ls):
    c = choose_best(t,k,ls)
    if c <= 0 : return None
    return c

# some guy
import itertools

def choose_best_sum(t, k, ls):
    return max(list(filter(lambda x: x >= 0 and x <= t, [sum(set) for set in list(itertools.combinations(ls, k))])), default=None)

# best solution
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((sum(v) for v in combinations(ls,k) if sum(v)<=t), default=None)
    

######################################################################################

# How many Integers in the range [0..n] contain at least one 9 in their decimal representation?
# nines :: Integer -> Integer
# nines n = length [x | x <- [0..n], x == 9 || x `mod` 10 == 9]
def nines(n):
    return sum(1 for x in range(n+1) if x == 9 or x % 10 == 9)


def nines(n):
    return sum(1 for i in range(n+1) if str(i).count('9') > 0)

# faster
def nines(n):
    s, r = str(n), 0
    for i, d in enumerate(s):
        r += int(d) * 9 ** (len(s) - i - 1)
        if d == '9':
            r -= 1
            break
    return n - r

# fastest
from re import sub
def nines(n):
    return n - int(sub(r'9.*$', lambda m: '8'*len(m[0]), str(n)), 9)
                    # sub( pattern, replacement, string )

print(nines(9750))