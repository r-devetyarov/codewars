""""
Дано положительное число. Найти сумму его цифр. Если передается не число "Подумай еще раз"
"""

from typing import Union


def sum_of_digits(some_number) -> Union[int, str]:
    if type(some_number) is not int:
        return "Подумай еще раз"
    return sum([int(i) for i in str(some_number)])


print(sum_of_digits(125))
print(sum_of_digits(0))
print(sum_of_digits(1231221123))
print(sum_of_digits('sasfa'))
print(sum_of_digits({'asdfa': "asfa"}))
