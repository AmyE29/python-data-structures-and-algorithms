class Node:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_table(self, key):
        hashed= 0
        for hash_index, i in enumerate(key):
            hashed += (hash_index+ len(key)) ** ord(i)
            hashed = hashed%self.size
        return hashed


    def add(self, key, value):
        bucket = self.hash_table(key)
        
        if not self.table[bucket]:
            self.table[bucket] = Node(key, value)
        else:
            temp = self.table[bucket]
            while temp.next:
                temp = temp.mext

    def get(self, key):
        bucket = self.hash_table(key)
        if self.table[bucket] is None:
            return None
        else:
            for i in self.table[bucket]:
                if i[0] == key:
                    return i[1]
    
    def find(self, key):
        bucket = self.hash_table(key)
        if self.table[bucket] is None:
            return None
        else:
            temp = self.table[bucket]
            while temp:
                if temp.key == key:
                    return temp.value
                temp = temp.next
            return None

    def delete(self, key):
        bucket = self.hash_table(key)
        if self.table[bucket] is None:
            return None
        else:
            if self.table[bucket].key == key:
                self.table[bucket] = None
            else:
                temp = self.bucket[key]
                while temp:
                    if temp.next.key == key:
                        temp.next = temp.next.next
                        return
                    temp = temp.next
                return None


