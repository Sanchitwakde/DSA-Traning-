# True, False and None has already inbuiilt things and has 1 letter capital 
# cognitiveclasses .ai ( for certificate )
# Aict internship portal for internship 


import sys
class getnode:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self):
        data = int(input("Enter data: "))
        newnode = getnode()
        newnode.data=data
        if self.head == None:
            self.head=newnode
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next=newnode
            print(data," is added")

    def traverse(self):
        if self.head==None:
            print("Linked List not present")

        else:
            ptr = self.head
            while ptr != None:
                print(ptr.data," -> ", end=" ")
                ptr=ptr.next
    def addBegin(self):
        data = int(input("Enter data: "))
        newnode = getnode()
        newnode.data=data
        if self.head == None:
            self.head=newnode
        else:
            #newnode.next = self.head
            #self.head = newnode

            ptr = self.head
            newnode.next = ptr
            self.head=newnode
            print("added at front")
    
    def addbetween(self):
        data = int(input("Enter data: "))
        key = int(input("Enter Key value: "))
        newnode = getnode()
        newnode.data=data
        if self.head == None:
            self.head=newnode
        else:
            ptr = self.head
            while ptr.next != None:
                if key == ptr.data:
                    break;
                else:
                    ptr=ptr.next
            if ptr.next==None:
                print("key not found")
            else:
                ptr1=ptr.next
                ptr.next=newnode
                newnode.next = ptr1
                print(data," is added")
                
    def delete_begin(self):
        if self.head==None:
            print("List is empty")
        else:
            ptr=self.head
            self.head = ptr.next
            print("Begin node is deleted")
    
    def delete_end(self):

        if self.head == None:
            print("List is empty ")

        ptr = self.head
        if ptr.next == None:
            self.head = None
            print("One and only Node deleted")
        
        else:
            ptr = self.head
            ptr1 = ptr.next

            while ptr1.next != None:
                ptr = ptr.next
                ptr1 = ptr1.next
               
            ptr.next = None
            print("last node deleted")


if __name__ == "__main__":
    obj = LinkedList()
    
    while True: 
        print("\n1. Append")
        print("2. Traverse")
        print("3. Add begin")
        print("4. Add inBetween")
        print("5. Delete at begin")
        print("6.Delete at end ")
        print("0. Exit")
        n = int(input("Select any Object: "))

        if n ==1:
            obj.append()
            obj.traverse()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.addBegin()
        elif n==4:
            obj.addbetween()
            obj.traverse()
        elif n==5:
            obj.delete_begin()
            obj.traverse()
        elif n==6:
            obj.delete_end()
            obj.traverse()
        elif n==0:
            sys.exit()

            