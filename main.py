
import sys
from stats import get_num_words, get_char_frequencies, sort_char_frequencies

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

try:
    with open(book_path, "r", encoding="utf-8") as f:
        book_text = f.read()
except FileNotFoundError:
    print(f"Error: File '{book_path}' not found.")
    sys.exit(1)

# Analyze
word_count = get_num_words(book_text)
char_freqs = get_char_frequencies(book_text)
sorted_char_freqs = sort_char_frequencies(char_freqs)

# Print the report
print("============ BOOKBOT =============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count -----------")
print(f"Found {word_count} total words")
print("--------- Character Count --------")

for entry in sorted_char_freqs:
    print(f"{entry['char']}: {entry['count']}")

print("============= END ================")
