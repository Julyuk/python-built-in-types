import python_philosophy as ph


def python_philosophy_formatter():
    str_to_format = ph.str_to_format
    occurrences_better = find_word_occurrences(str_to_format, "better")
    print(f"Occurrences of 'better': {occurrences_better}")
    occurrences_never = find_word_occurrences(str_to_format, "never")
    print(f"Occurrences of 'never': {occurrences_never}")
    occurrences_is = find_word_occurrences(str_to_format, "is")
    print(f"Occurrences of 'is': {occurrences_is}")
    str_to_format = replace_symbol(str_to_format, "i", "&")
    str_to_format = make_string_uppercase(str_to_format)
    print(str_to_format)
    return str_to_format


def make_string_uppercase(str_to_format):
    return str_to_format.upper()


def replace_symbol(str, initial, new):
    return str.lower().replace(initial, new)


def find_word_occurrences(str_to_format, word):
    occurrences = str_to_format.lower().count(word)
    return occurrences


