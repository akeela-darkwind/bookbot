#set up book document retrieve
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        
        return f.read(), path_to_file
               
#word counting import from stats.py
from stats import number_of_words

#character counting import from stats.py
from stats import character_counts

#report format import from stats.py
from stats import create_report

#set input for book location (path must be in quotes) and assign to variable for export
def main():
    book_path = "books/frankenstein.txt"
    contents, path = get_book_text(book_path)
    num_words = number_of_words(contents)
    num_chars = character_counts(contents)
    char_report = create_report(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in char_report:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")

    print("============= END ===============")    
    #print(num_chars)
    #print(char_report)
    #print(contents)
    

#call to make it work from cli
main()