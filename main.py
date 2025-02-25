#set up book document retreival
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
   
#set input for book location (path must be in quotes) and assign to variable for print
def main():
    contents = get_book_text("books/frankenstein.txt")
    print(contents)
    

#call to make it work from cli
main()