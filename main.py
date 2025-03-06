import sys
from stats import count_words
from stats import count_characters
from stats import sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    word_count = count_words(get_book_text(path))
    char_count = count_characters(get_book_text(path))
    sorted_count = sorted_dict(char_count)

    char_count_section = ""
    for char_dict in sorted_count:
        char = char_dict["character"]
        count = char_dict["count"]
        char_count_section += f"{char}: {count}\n"
    
    report = f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{char_count_section}============= END ==============="""

    print(report)

main()