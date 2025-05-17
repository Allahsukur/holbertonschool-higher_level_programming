#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        list_range = range(0, x)
        for i in list_range:
            try:
                print("{:d}".format(my_list[i]), end='')
                count += 1
            except (TypeError, ValueError):
                continue
        print()
    except (IndexError, TypeError):
        print()
    return count
