r""""
Write a function that takes an array of numbers (integers for the tests) and a target number.
It should find two different items in the array that, when added together, give the target value.
The indices of these items should then be returned in a tuple like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
target will always be the sum of two different items from that array).
"""
from typing import List, Tuple


def two_sum(numbers: List[int], target: int) -> Tuple[int, int]:
    index_1, index_2 = None, None
    for number in range(len(numbers)):
        for item in range(len(numbers)):
            if numbers[number] + numbers[item] == target:
                index_1 = number
                index_2 = item
                break
    if index_1 < index_2:
        return index_1, index_2
    else:
        return index_2, index_1


if __name__ == '__main__':
    print(two_sum([1, 2, 3], 4))
    print(two_sum([1234, 5678, 9012], 14690))
    print(two_sum([2, 2, 3], 4))
