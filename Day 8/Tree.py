# left side of tree will have less value than root 
# right will have more value than root 
import sys

class bst:
    def __init__(self,key):
        self.leftchild = None
        self.data = key
        self.rightchild = None

    def insert(self,key):
        if self.data ==None: # to insert node if not exist 
            self.data = key
            return
        elif self.data == key: # to check duplicate 
            return
        else:
            if key < self.data:
                if self.leftchild:
                    self.leftchild.insert(key)
                else:
                    self.leftchild = bst(key)
            elif key > self.data:
                if self.rightchild:
                    self.rightchild.insert(key)
                else:
                    self.rightchild=bst(key)

    def preorder(self):
        print(self.data,end="->")
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        print(self.data,end="->")
        if self.rightchild:
            self.rightchild.inorder()
    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        
        if self.rightchild:
            self.rightchild.postorder()

        print(self.data,end="->")

    def search(self,key):
       
        if self.data == None:
                self.data = key
                print("key not found")
        elif self.data is key:
                print("key is found ",key)
        else: 
            print("key not found")

        if key < self.data:
            if self.leftchild:
                self.leftchild.search(key)
            else:
                self.leftchild = bst(key)
        elif key > self.data:
            if self.rightchild:
                self.rightchild.search(key)
            else:
                self.rightchild = bst(key)
            
        


        

if __name__ == '__main__':
    root=bst(None)
    while True:
        print("\n1. Insert")
        print("2. Preorder")
        print("3. Inorder")
        print("4. Postorder")
        print("5. Search")
        print("0. Exit")

        n = int(input("Enter your Option:"))

        if n==1:
            arr = [36,26,46,21,31,11,24,41,56,51,66]
            for i in range(len(arr)):
                root.insert(arr[i])

        elif n==2:
            root.preorder()
        elif n==3:
            root.inorder()
        elif n==4:
            root.postorder()
        elif n==5:
            keys = int(input("Enter key you want to search: "))
            root.search(keys)
            
        elif n==0:
            sys.exit()