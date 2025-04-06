import sys
from stats import count_char_repeated, count_words, sort_by_count_reverse

def get_book_text(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def main(file_path: str) -> None:
    book_text = get_book_text(file_path)

    word_counts = count_words(book_text)
    char_count = count_char_repeated(book_text)
    sorted_char_count = sort_by_count_reverse(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_count.items():
        if char.isalpha() is not True:
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
