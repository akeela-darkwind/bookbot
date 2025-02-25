#set up book document retrieve
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

#word counting import from stats.py
from stats import number_of_words

#set input for book location (path must be in quotes) and assign to variable for export
def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(contents)
    print(f"{num_words} words found in the document")
    #print(contents)
    

#call to make it work from cli
main()