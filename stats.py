def get_book_test(filepath):
    with open(filepath) as file:
        lines = file.read()
        return lines


def get_number_of_words(text):
    dict_char = {}
    for char in text:
        char = char.lower()
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1
    return dict_char


def sort_dict(dict_char):
    # ensure key is alphanumeric
    dict_alpha = {k: v for k, v in dict_char.items() if k.isalpha()}
    # sort dict in reversed order by value
    sorted_dict = dict(
        sorted(
            dict_alpha.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )
    return sorted_dict
