#graph has types 
#directed graph , undirected graph, complete graph and cyclic and acyclic graph 
# also there are directed + unweighted, weighted + undirected , undirected + unweighted ,undirected + weighted
import sys
class Graph:
    def __init__(self):
        self.nodes=[]
        self.nodecount=0
        self.graph=[]
    def addnode(self,v):
        if v in self.nodes:
            print(v,"is already present")
        else:
            self.nodecount+=1
            self.nodes.append(v)
            for x in self.graph:
                x.append(0)
            temp =[]
            for x in range(self.nodecount):
                temp.append(0)
            self.graph.append(temp)
            print(v,"is added")

    def addedge_undirected_unweighted(self,v1,v2):
        if v1 not in self.nodes:
            print(v1, " not present ")
            return
        if v2 not in self.nodes:
            print(v2, " not present ")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2]=1
        self.graph[index2][index1]=1

    def addedge_undirected_weighted():
        pass
    def addedge_directed_weighted():
        pass
    def printgraph(self):
        print(" ",*self.nodes)
        for i in range(self.nodecount):
            print(self.nodes[i]," ")
            for j in range(self.nodecount):
                print(self.graph[i][j],end = " ")
            print()

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
            v = input("Enter vertex: ")
            obj.addnode(v)
        elif n==2:
            v1=input("Enter Vertex 1")
            v2 = input("Enter Vertex 2")
            obj.addedge_undirected_unweighted(v1,v2)
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