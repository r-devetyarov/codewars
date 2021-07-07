def mixed_fraction(string: str):
    number_list = list(map(int, string.split('/')))
    print(number_list)
    if number_list[0] % number_list[1] == 0:
        result = f"{number_list[0] // number_list[1]}"

    mixed_fraction('-42/9')



