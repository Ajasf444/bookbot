from stats import count_characters, count_words, get_text, print_report, sort_chars


def main():
    frankenstein_path = "./books/frankenstein.txt"
    text = get_text(frankenstein_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_char_list = sort_chars(char_count)
    print_report(frankenstein_path, word_count, sorted_char_list)


if __name__ == "__main__":
    main()

