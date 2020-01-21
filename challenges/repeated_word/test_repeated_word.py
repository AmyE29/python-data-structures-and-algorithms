import pytest
from repeated_word import repeated_word


def test_string():
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn\'t know what I was doing in New York..."
    word = repeated_word(string)
    assert word == 'summer'

def test_not_repeated():
    string = "Apple banana cat dog elephant fruitfly."
    word = repeated_word(string)
    assert word == None

def test_punctuation():
    string = "It was a queer, sultry summer!!!!, the summer? they electrocuted the Rosenbergs, and I didn\'t know what I was doing in New York..."
    word = repeated_word(string)
    assert word == 'summer'

def test_capitalization():
    string = "It was a queer, sultry SUMmer, the summer they electrocuted the Rosenbergs, and I didn\'t know what I was doing in New York..."
    word = repeated_word(string)
    assert word == 'summer'

def test_long_random_string():
    string = "Apple apricot alpaca banana Bermuda boat cat catnip catsup, or is it ketchup?, dog doll dogstar doggie Eyeore eyesore eye flight fright fight great greater grate holliday Hollywood Halle Berry igloo ignore ignatious jelly jealous jellybean jeans kettle should have put ketchup here llama mama pajama drama "	
    word = repeated_word(string)
    assert word == 'ketchup'



 