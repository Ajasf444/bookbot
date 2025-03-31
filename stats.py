def count_words(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    char_count_dict = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char not in char_count_dict:
            char_count_dict[char] = 0
        char_count_dict[char] += 1
    return char_count_dict


def _char_list(char_dict: dict):
    return [{"char": k, "count": v} for k, v in char_dict.items()]


def sort_on(dict):
    return dict["count"]


def sort_chars(char_count):
    char_list = _char_list(char_count)
    char_list.sort(reverse=True, key=sort_on)

    return char_list


def print_report(path, word_count, char_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for char_dict in char_list:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"The '{char}' character was found {count} times")
