# enumerate - gives index of key and values in dictionary

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for i in range(size)]
    
    def hash_function(self,key):
        return key % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        self.table[index].append((key,value))
    def search(self,key):
        index = self.hash_function(key)
        for k,v in self.table[index]:
            if k == key:
                return v
        return "Not found"
    
    def delete(self,key):
        index = self.hash_function(key)

        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
            
    def display(self):
        print(self.table)

h = HashTable(10)

h.insert(11,"pikachu")
h.insert(22,"Charmander")
h.insert(33,"Balbasaur")
h.insert(44,"Squirtle")
h.display()

h.delete(33)
h.display()