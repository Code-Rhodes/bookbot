import sys

from stats import get_num_words, get_lower_count, sort_char_counts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_num_words(text)

    char_counts = get_lower_count(text)

    sorted_chars = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path + "...")
    print("----------- Word Count ----------")
    print("Found " + str(num_words) + " total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(item["char"] + ": " + str(item["num"]))
    print("============= END ===============")

def get_book_text(path):
    with open(path, encoding="UTF-8") as f:
        return f.read()


main()
