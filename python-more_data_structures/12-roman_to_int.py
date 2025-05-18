#!/usr/bin/python3

def roman_to_int(roman_string):
    rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rs = roman_string
    number = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return number
    for i in range(len(rs)):
        if i + 1 < len(rs) and rn[rs[i]] < rn[rs[i+1]]:
            number -= rn[rs[i]]
        else:
            number += rn[rs[i]]
    return number
