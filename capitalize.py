""""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately,
 and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity
"""
from typing import List


def capitalize(s: str) -> List[str]:
    case_1 = case_2 = ''
    for i in range(len(s)):
        if i == 0 or i % 2 == 0:
            case_1 += s[i].upper()
            case_2 += s[i]
        else:
            case_1 += s[i]
            case_2 += s[i].upper()
    return [case_1, case_2]


print((capitalize("abcdef"), ['AbCdEf', 'aBcDeF']))
