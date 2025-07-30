
from stats import count_chars_in_text, get_word_count, create_dicts
import sys


def get_book_text(filename):
    with open(filename) as f:
        # do something with f (the file) here
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]
    book_text = get_book_text(book_location)
    word_count = get_word_count(book_text)
    chars_list = create_dicts(count_chars_in_text(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in chars_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()
