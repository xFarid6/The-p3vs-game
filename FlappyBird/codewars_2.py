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

# expressing an ordered list of integers using a comma separated list of either
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. 
def solution(l):
    return ','.join(['-'.join(map(str, range(i, j + 1))) if j - i >= 2 else str(i) for i, j in zip(l, l[1:])])