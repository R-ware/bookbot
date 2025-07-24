import sys
from stats import get_word_count, get_char_count, get_sorted
    

def get_book_text(filepath):
        with open(filepath) as f:
            return f.read()

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    num_chars = get_char_count(book_text)
    sorted_char_counts = get_sorted(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----")
    for item in sorted_char_counts:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")
    
main()