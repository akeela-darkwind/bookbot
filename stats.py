#accept text from book as string; returns # of words in the string
def number_of_words(contents):
    word_list = contents.split()
    return len(word_list)

# takes text from book and returns # of times each character (incl symbols and spaces) appears
def character_counts(contents):
    converted_case = str.lower(contents)
    characters = {}

    for case in converted_case:
        if case in characters:
            characters[case] += 1
        else:
            characters[case]  = 1
    return characters

