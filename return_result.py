# 0 отзывов, 1 отзыв, 2 отзыва, 5 отзывов, 21 отызв, 111 отзывовов, 102 отзыва
def return_result(count: int) -> str:
    final_str = ''
    last_symbol, last_2_symbols = int(str(count)[-1]), int(str(count)[-2:])
    if 10 <= last_2_symbols <= 20 or last_symbol >= 5 or last_symbol == 0:
        final_str = 'ов'
    elif 5 > last_symbol > 1:
        final_str = 'а'

    return f"{count} отзыв{final_str}"


for i in range(0, 10001):
    print(return_result(i))
