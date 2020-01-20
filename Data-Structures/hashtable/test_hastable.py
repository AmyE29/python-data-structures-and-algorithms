from hashtable import HashTable

def test_added():
    hash_table = HashTable(0)
    hash_table.add('fruit','apple')
    expected = 1
    actual = hash_table.size
    assert actual == expected


def test_get():
    hash_table = HashTable(0)
    hash_table.add('fruit', 'apple')
    expected = 'apple'
    actual = hash_table.get('fruit')
    assert actual == expected

def test_not_included():
    hash_table = HashTable(0)
    hash_table.add('fruit', 'apple')
    expected = None
    actual = hash_table.find('vegetable')
    assert actual == expected

def test_collision():
    hash_table = HashTable(0)
    hash_table.add('cat', 'Jingles')
    hash_table.add('tac', 'ouchy')
    actual = 2
    expected = hash_table.size
    assert actual == expected

def test_collision_get():
    hash_table = HashTable(0)
    hash_table.add('cat', 'Jingles')
    hash_table.add('tac', 'ouchy')
    actual = 'ouchy'
    expected = hash_table.get('tac')
    assert actual == expected