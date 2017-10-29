from __future__ import print_function


def SolutionOne(string1, string2):
    # Convert the second string to list for convenience to remove the character
    # from it.
    string2_list = list(string2)
    for char in string1:
        # If character is in the second string, remove it and continue with the
        # loop
        if char in string2_list:
            string2_list.remove(char)
        # If the character is not in string2, return False.
        else:
            return False
    else:
        # After the loop ends, if there is nothing remaining in the list,
        # return True else False
        return not string2_list


def SolutionTwo(string1, string2):
    return sorted(string1) == sorted(string2)


def SolutionThree(string1, string2):
    # If lengths of both the strings are different, directly return False
    if len(string1) != len(string2):
        return False
    lookup = {}
    # Filling the lookup from string1
    for char in string1:
        # Assuming that the character already exists in the lookup
        try:
            lookup[char] += 1
        # If not, just except the error and add the character with occurrence 1
        except KeyError:
            lookup[char] = 1
    # Reversing the process with string2
    for char in string2:
        # Assuming that the character already exists in the lookup
        try:
            lookup[char] -= 1
        # If not, return False
        except KeyError:
            return False
    # At the end, if total occurrences of all the character left is 0,
    # return True
    return sum(lookup.values()) == 0
