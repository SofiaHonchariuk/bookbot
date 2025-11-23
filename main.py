import sys
from stats import count_words, count_characters, sorted_list_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    #filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)

    num_words = count_words(text)
    counter_c = count_characters(text)
    list_of_dict = sorted_list_dict(counter_c)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in list_of_dict:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
        
    print("============= END ===============")
  


main()