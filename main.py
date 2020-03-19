"""
Program to determine whether a one-to-one character mapping exists from one string, s1, to another string,
s2.
"""

# User input variables
s1 = list(input('Please enter string 1: '))
s2 = list(input('Please enter string 2: '))

def one_one_mapping(s1, s2):
    # Checking for different lengths
    if len(s1) != len(s2):
        return False
    else:
        # Checking for repetition
        if len(s1) == len(set(s1)):
            return True
        else:
            return False
        
print(one_one_mapping(s1, s2))