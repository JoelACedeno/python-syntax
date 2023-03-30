def print_upper_words(words):
    """For a list of words, prints out each word on a separate line but in all uppercase. """
    for word in words:
        print(word.upper())

    
def print_upper_words2(words):
    """same as print_upper_words, but only prints words that start with the letter 'e' """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, starting_with):
    """same as print_upper_words, ONLY if word starts with the given letter"""
    for word in words:
        for letter in starting_with:
            if word.startswith(letter):
                print(word.upper())