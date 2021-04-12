""""
Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)
"""


def find(n: int) -> int:
    return sum([integer for integer in range(n + 1) if integer % 3 == 0 or integer % 5 == 0])
