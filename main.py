#set up book document retrieve
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

#accept text from book as string; returns # of words in the string
def number_of_words(contents):
    word_list = contents.split()
    return len(word_list)


#set input for book location (path must be in quotes) and assign to variable for export
def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(contents)
    print(f"{num_words} words found in the document")
    #print(contents)
    

#call to make it work from cli
main()