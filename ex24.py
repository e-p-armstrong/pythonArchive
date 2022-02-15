def breakwords(arg):
    """This function does something that a prebuilt haskell function does already"""
    words = arg.split(' ')
    return words

def sortwords(words):
    """Sorts words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after removing it from the list"""
    word = words.pop(0)
    print(word)

def printlastword(words):
    """Prints the first word after removing it from the list"""
    word = words.pop(-1)
    print(word)

def sortsentence(sentence):
    """Sorts the words of a sentence"""
    words = breakwords(sentence)
    return sortwords(words)
    
def firstlast(words):
    """I wonder what this does"""
    print_first_word(words)
    printlastword(words)


def sortedfirstlast(words):
    x = sortsentence(words)
    print_first_word(x)
    printlastword(x)