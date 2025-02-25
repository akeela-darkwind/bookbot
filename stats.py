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

# creates a sorted dictionary for reporting
def sort_on(dict):
    return list(dict.values())[0]

def create_report(characters):
    chars_list = []

    for char, count in characters.items():
        letter = {char: count}
        chars_list.append(letter)
    
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
    