#inheritance 
#--------------------------------------------------------------
#single 
class a:
    def showa(self):
        print("I am class a")
class b(a):
    def showb(self):
        print("i am class b")

if __name__ == '__main__':
    obj=b()
    obj.showa()
    obj.showb()
#--------------------------------------------------------------
#multi level
class a:
    def showa(self):
        print("I am class a")
class b(a):
    def showb(self):
        print("i am class b")
class c(b):
    def showc(self):
        print("i am in class c")

if __name__ == '__main__':
    obj=c()
    obj.showa()
    obj.showb()
    obj.showc()

#--------------------------------------------------------------
#hybrid 
#     class a 
# |           |
# class b   class c 
#   |         |
#    class d
#--------------------------------------------------------------
#multiple 
# class a  class b
#        |
#     class c

#--------------------------------------------------------------

#hierarchical 

#       class d
#    |        |      |
# classA   classB   classC

