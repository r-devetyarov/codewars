""""
Дано целое число n. Вернуть наибольшее число, содержащее n цифр
n = 4 -> 9999
n = 1 -> 9
"""


def largest_number(digit: int) -> int:
    return 10 ** digit - 1


print(largest_number(4))
print(largest_number(0))
print(largest_number(1))
print(largest_number(2))
print(largest_number(8))
