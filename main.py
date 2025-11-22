import sys
from stats import get_num_words
from stats import get_char_num
from stats import get_sorted_dict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book = sys.argv[1]
    strings = get_book_text(book)
    dict = {}
    dict = get_char_num(strings)
    sorted_dict = get_sorted_dict(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(strings)} total words")
    print("--------- Character Count -------")
    for k, v in sorted_dict.items():
        print(f"{k}: {v}")
    print("============= END ===============")


main()
