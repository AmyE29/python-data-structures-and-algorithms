import re

def repeated_word (str):
    str = re.sub (r'[^\w\s]', '', str)
    wordset = []
    words = str.lower().split()

    for word in words:
        if word in wordset:
            return word
        wordset.append(word)
    return None
