import sys  #to exit the program

class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5

    def isFull(self):
        if self.top == self.CAPACITY-1:
            return True
        else:
            return False
    
    def push(self,ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele, "is pushed")
    
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])   
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")            
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top-=1
            print(ele, " is Popped")
        
    def peek(self):
        print(self.stack[self.top])

class Queue:
    def __init__(self): #constructor
        self.queue = []
        self.rear = -1
        self.front = 0
        self.capacity = 5
    
    def isFull(self):
        if self.front == self.capacity-1:
            return True
        else:
            return False
        
    def insert(self,ele):
        if self.isFull():
            print("Queue is full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print(ele," is inserted")
            print()
    
    def traverse(self):
        if self.isEmpty():
            print("Queue is empty ")
        for i in range(self.rear+1):
            print(self.queue[i],end = " ")
        print()
        print()
    
    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False
        
    def delete(self):
        if self.isEmpty():
            print(" Queue is empty")
        else:
            ele = self.queue[self.front] # to store a element that willl be deleted
            for i in range(1,self.rear+1):
                self.queue[i-1]=self.queue[i]
            self.rear-=1
            print(ele," is deleted")
        return ele 
        
    def fpeek(self):
        print("Front element: ",self.queue[self.front])
        
    def rpeek(self):    
        print("Last element: ",self.queue[self.rear])




if __name__ == '__main__':
    obj1 = Queue()
    obj2 = Stack()
    n = int(input("enter no. of element: "))

    for i in range(n):
        ele = int(input("Enter Element: "))
        obj1.insert(ele)
    obj1.traverse()
    for x in range(n):
        ele = obj1.delete()
        obj2.push(ele)
    obj2.traverse()
    for y in range(n):
        ele = obj2.pop()
        obj1.insert(ele)
    
    obj1.traverse()