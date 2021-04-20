"""
Содержит ли массив из целых чисел дубликаты : -> bool
"""
from typing import List


def contains_duplicates(ex_list: List[int]) -> bool:
    for element in ex_list:
        if ex_list.count(element) > 1:
            return True
    return False


def contains_duplicates_2(ex_list: List[int]) -> bool:
    return len(ex_list) != len(set(ex_list))


print(contains_duplicates_2([1, 2, 3, 10, 1]))
print(contains_duplicates_2([i for i in range(10)]))
print(contains_duplicates_2([]))
