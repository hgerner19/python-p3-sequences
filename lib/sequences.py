#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []
    i = 0
    j = 0

    while i < length:
        if len(my_list) == 0:
            my_list.append(j)
            j += 1
        else:
            if len(my_list) <= 2:
                value = my_list[i-1]
                j += value
                my_list.append(j)
                j = 0
            else:
                value = my_list[i-1] + my_list[i-2]
                j+=value
                my_list.append(j)
                j = 0
        i += 1
    print(my_list)

    pass