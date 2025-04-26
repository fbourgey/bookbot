import sys
from stats import get_book_test, get_number_of_words, sort_dict


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    # filepath = "books/frankenstein.txt"
    filepath = sys.argv[1]
    text = get_book_test(filepath)
    num_words = len(text.split())
    dict_words = get_number_of_words(text)
    dict_sorted = sort_dict(dict_words)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in dict_sorted.items():
        print(f"{k}: {v}")
    print("============= END ===============")
    return None


if __name__ == "__main__":
    main()

main()
