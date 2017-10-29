from __future__ import print_function


def Solution(input_string, length):
    # We know that the last non-space character will be replaced at the last
    # index of the whole string. Hence the replace index will be the last index
    # initially.
    replaced_idx = len(input_string)
    # Starting from the end for inplace transformation
    for idx in reversed(range(length)):
        # If the current character is space, replace the place to be replaced
        # at with 3 characters instead of one and move replace index by 3.
        if input_string[idx] == ' ':
            input_string[replaced_idx - 3:replaced_idx] = '%20'
            replaced_idx -= 3
        # If the current character is not a space move the character as it is
        # to the replace index and move the replace index by one.
        else:
            input_string[replaced_idx - 1] = input_string[idx]
            replaced_idx -= 1
    return input_string
