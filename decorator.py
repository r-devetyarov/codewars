import time


def func_time(func):
    print("Before")

    def wrapper(*args, **kwargs):
        return func(*args)

    final = wrapper

    print("nen")
    return final


@func_time
def my_sum():
    print("Сама функция")


my_sum()
