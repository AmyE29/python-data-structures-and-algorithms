from join import join
import pytest


def test_join():
    table1 = {
        'food':'apple',
        'car':'Ford',
        'shoe':'boot',
        'expression':'happy',
        }
    table2 = {
        'food':'banana',
        'car':'Chevy',
        'expression':'sad',
        'pet':'cat'
        }

    actual = join(table1, table2)
    expected = [
        ['food','apple','banana'],
        ['car','Ford','Chevy'],
        ['expression', 'happy', 'sad'],
        ['shoe','boot', None],
    
    ]
    assert actual == expected

def test_empty_table1():
    table1 = {
        }
    table2 = {
        'food':'banana',
        'car':'Chevy',
        'expression':'sad',
        'pet':'cat'
        }

    actual = join(table1, table2)
    expected = []
    assert actual == expected

def test_empty_table2():
    table1 = {
        'food':'apple',
        'car':'Ford',
        'shoe':'boot',
        'expression':'happy',
        }
    table2 = {
        }

    actual = join(table1, table2)
    expected = [
        ['food','apple',None],
        ['car','Ford', None],
        ['expression', 'happy', None],
        ['shoe','boot', None],
    
    ]
    assert actual == expected

def test_no_common():
    table1 = {
        'food':'apple',
        'car':'Ford',
        'shoe':'boot',
        'expression':'happy',
        }
    table2 = {
        'fruit':'banana',
        'drive':'Chevy',
        'shop':'book',
        'excited':'glad',
        }

    actual = join(table1, table2)
    expected = [
        ['food','apple',None],
        ['car','Ford', None],
        ['expression', 'happy', None],
        ['shoe','boot', None],
    
    ]
    assert actual == expected
