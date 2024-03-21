#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxlen = my_list[0]
    for num in my_list[1:]:  # Or range(1, len(my_list)):
        if maxlen < num:
            maxlen = num
    return maxlen
