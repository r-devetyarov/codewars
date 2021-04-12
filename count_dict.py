from typing import Dict


def count(string: str) -> Dict[str, int]:
    symbol_set = set()
    final_dict = dict()
    for symbol in string:
        symbol_set.add(symbol)
    for symbol in symbol_set:
        final_dict[symbol] = string.count(symbol)
    return final_dict


if __name__ == '__main__':
    print(count('aba'), {'a': 2, 'b': 1})
    print(count(''), {})


def cont_new(string: str) -> Dict[str, int]:
    return {i: string.count(i) for i in string}


print(cont_new('aba'), {'a': 2, 'b': 1})
