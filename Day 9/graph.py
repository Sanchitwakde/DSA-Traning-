#graph has types 
#directed graph , undirected graph, complete graph and cyclic and acyclic graph 
# also there are directed + unweighted, weighted + undirected , undirected + unweighted ,undirected + weighted
import sys
class Graph:
    def __init__():
        pass
    def addnode():
        pass
    def addedge_undirected_unweighted():
        pass
    def addedge_undirected_weighted():
        pass
    def addedge_directed_weighted():
        pass
    def printgraph():
        pass
    def deletegraph():
        pass
    
if __name__ == '__main__':
    obj = Graph()
    while True:
        print("\n1. (insertion) Add a node using adjacency matrix representation")
        print("2. (insertion) Add a edge using adjacency matrix representation")
        print("3. (insertion) Add a edge undirected weighted graph")
        print("4. (insertion) Add a edge directed weighted graph")
        print("5. Print Graph")
        print("6. Delete Operation")
        print("0. Exit\n")
        n=int(input("Enter any choice: "))
        if n==1:
            obj.addnode()
        elif n==2:
            obj.addedge_undirected_unweighted()
        elif n==3:
            obj.addedge_undirected_weighted()
        elif n==4:
            obj.addedge_directed_weighted()
        elif n==5:
            obj.printgraph()
        elif n==6:
            obj.deletegraph()
        elif n==0:
            sys.exit(0)