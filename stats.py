#accept text from book as string; returns # of words in the string
def number_of_words(contents):
    word_list = contents.split()
    return len(word_list)
