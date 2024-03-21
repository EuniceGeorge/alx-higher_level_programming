#!/usr/bin/python3
def max_integer(my_list=[]):
    for in my_list == 0:
        if len(my_list) == 0:
            return None
        elif len(my_list) == 1:
            return my_list[0]
        maxlen == my_list[0]
        for i in my_list[1:]:
            if i > maxlen:
                maxlen = i
        return maxlen
