from __future__ import print_function


def SolutionOne(string_input):
    # Throwing the string into set to make everythin unique
    string_set = set(string_input)
    return len(string_input) == len(string_set)


def SolutionTwo(string_input):
    # Constant Lookup for 128 Characters in ASCII
    # Initializing with False for already seen initially.
    lookup = [False] * 128
    for char in string_input:
        # Taking ascii value for lookup index
        ascii_value = ord(char)
        # If not seen earlier
        if not lookup[ascii_value]:
            # Make it seen now
            lookup[ascii_value] = True
        # If seen earlier
        else:
            return False
    # Successful exit from the loop means there was no character that was seen
    # after being seen once
    else:
        return True


def SolutionThree(string_input):
    # Checking for the short-circuit condition to return if the length of
    # string is more that all possible unique ascii characters
    if len(string_input) > 128:
        return False
    # Constant Lookup for 128 Characters in ASCII
    # Initializing with False for already seen initially.
    lookup = [False] * 128
    for char in string_input:
        # Taking ascii value for lookup index
        ascii_value = ord(char)
        # If not seen earlier
        if not lookup[ascii_value]:
            # Make it seen now
            lookup[ascii_value] = True
        # If seen earlier
        else:
            return False
    # Successful exit from the loop means there was no character that was seen
    # after being seen once
    else:
        return True
