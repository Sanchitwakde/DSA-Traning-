# enumerate - gives index of key and values in dictionary

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for i in range(size)]
    
    def hash_function(self,key):
        return key % self.size
    
    def insert(self,key,value):
        index = self.hash_function