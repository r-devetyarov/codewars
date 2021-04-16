""""
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text: str) -> str:
    word_arr = text.split(' ')
    final_text = ''
    for word in word_arr:
        final_text += f"{word[::-1]} "
    return final_text[:-1]
    # or
    # return ' '.join((word[::-1] for word in text.split(' ')))



print(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
print(reverse_words('apple'), 'elppa')
print(reverse_words('a b c d'), 'a b c d')
print(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')
