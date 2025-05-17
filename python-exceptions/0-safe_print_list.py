#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in range(x):
            print(my_list[element], end='')
            count += 1
        print()
    except (IndexError, TypeError):
        print()
    return count
