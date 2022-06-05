# return the last digit of the decimal representation of a fibonacci number at index idx
def get_last_digit(index):
    if index == 0: return 0
    if index == 1: return 1
    fib = [0, 1]
    for i in range(2, index+1):
        fib.append((fib[i-1] + fib[i-2]) % 10)
    return fib[-1]

def get_last_digit(index):
    a, b = 0, 1
    for _ in range(index):
        a, b = b, (a+b) % 10
    return a


###############################################

# return the last digit of the decimal representation of a fibonacci number at index n
# no bruteforce
def get_last_digit(n):
    if n == 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, (a+b) % 10
    return b


def get_last_digit(index):
    return [0,1,1,2,3,5,8,3,1,4,5,9,4,3,7,0,7,7,4,1,5,6,1,7,8,5,3,8,1,9,0,9,9,8,7,5,2,7,9,6,5,1,6,7,3,0,3,3,6,9,5,4,9,3,2,5,7,2,9,1][index%60]


###############################################

# return the sum of two lists as matrices
def matrix_addition(m1, m2):
    return [[a+b for a, b in zip(i, j)] for i, j in zip(m1, m2)]

import numpy as np
def matrix_addition(a, b):
    return(np.mat(a)+np.mat(b)).tolist()


###############################################

# create a regex to evaluate binary string and determining whether the given string represents a number divisible by 3.
def is_divisible_by_3(s):
    return re.match(r'^[10]*0$', s) and s[-1] == '0'

# create a regex to evaluate binary string and determining whether the given string represents a number divisible by 3
# count the number of non-zero odd positions bits and non-zero even position bits from the right. 
# If their difference is divisible by 3, then the number is divisible by 3.
def is_divisible_by_3(s):
    return re.match(r'^[10]*0$', s) and (s.count('1') - s.count('0')) % 3 == 0

PATTERN = re.compile(r'^[10]*0$')

PATTERN = re.compile(r'^(0|1(01*0)*1)*$') #ok