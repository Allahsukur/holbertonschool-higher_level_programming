#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            count += 1
        if x > count:
            raise IndexError
        for element in range(x):
            print(my_list[element], end='')
        print()
        return count
    except IndexError:
        return count