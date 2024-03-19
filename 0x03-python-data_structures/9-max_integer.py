#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        if len(my_list) == 0:
            return None
        elif len(my_list) == 1:
            return my_list[0]
        elif my_list[i] < my_list[i+1]:
            return my_list[i+1]
        else:
            return my_list[i]
