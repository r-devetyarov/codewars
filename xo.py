""""
return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""


def xo(s: str) -> bool:
    s = s.lower()
    return s.count('x') == s.count('o')


if __name__ == '__main__':
    print(xo('xo'), 'True expected')
    print(xo('xo0'), 'True expected')
    print(xo('xxxoo'), 'False expected')
