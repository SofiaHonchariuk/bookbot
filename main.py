def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    number_of_words = 0 
    for i in words:
        number_of_words += 1
    return(number_of_words)

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words") 
  

main()