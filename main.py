import sys

from stats import (
    get_num_words, 
    get_num_characters, 
    get_sorted_list,
)

def get_book_text(filepath):
    return open(filepath, "r").read()

def main():
    if sys.argv[1:]:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_list = get_sorted_list(get_num_characters(text))
    print_report(book_path, num_words, sorted_list)


def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()