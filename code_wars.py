import string


def likes(names: list):
    list_count = len(names)

    if list_count == 0:
        return "no one likes this"
    if list_count == 1:
        return f"{names[0]} likes this"
    if list_count > 1:
        if list_count == 2:
            return f"{names[0]} and {names[1]} like this"
        else:
            if list_count == 3:
                return f"{names[0]}, {names[1]} and {names[2]} like this"
            else:
                return f"{names[0]}, {names[1]} and {list_count - 2} others like this"


def is_pangram(text) -> bool:
    array_text = []
    print(string.ascii_lowercase)
    for symbol in text:
        array_text.append(symbol)
    array_symbol = []
    for element in array_text:
        if element not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '?', '.', ',', ' ', '-', '_', "'"]:
            array_symbol.append(element.lower())
    flag = True
    for element in array_symbol:
        if element.lower() not in string.ascii_lowercase:
            flag = False
            break
        for symbol in string.ascii_lowercase:
            if symbol not in array_symbol:
                flag = False
                break
    return flag


# pangram = "abcdefghijklmopqrstuvwxyz"
# print(is_pangram(pangram))
def func(**kwargs):
    for args, value in kwargs.items():
        print(args, value)


