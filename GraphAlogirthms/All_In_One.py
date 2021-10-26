import collections
from collections import deque
stack = []
dfs_list = []
dfs_finish = []
bfs_list = []
class Graph:
    def __init__(self):
        self.components = 0
        self.counter = 1
        self.cycle = False
        self.root = []
        self.articulationPoints = []
        self.artCount = 1
        self.tStack = []

    def dfs(self,graph_vertex_list,startVertex):
        startVertex.startTime = self.counter
        self.counter = self.counter + 1
        if startVertex.color == 0:
            startVertex.color= 1
            dfs_list.append(startVertex)

        #stack.append(startVertex)
        for node in startVertex.adjacencyList.keys():
            if node.color == 0:
                node.parent = startVertex
                self.dfs(graph_vertex_list, node)
            elif node.color == 1 and startVertex.parent != None and startVertex.parent != node:
                self.cycle = True

        startVertex.color = 2
        startVertex.finishTime = self.counter
        self.counter = self.counter + 1
        dfs_finish.append(startVertex)
        # while (len(stack)>0):
        #     s = stack[-1]
        #
        #     if s.color == 0:
        #         s.color = 1
        #         dfs_list.append(s)
        #
        #     for node in s.adjacencyList.keys():
        #         if node.color == 0:
        #             self.dfs(graph_vertex_list,node)
        #     s.color = 2
        #     s.finishTime = self.counter
        #     self.counter = self.counter+1
        #     if len(stack)>0:
        #         stack.pop()

        return

    def driving_dfs(self,graph_vertex_list,startVertex):
        self.dfs(graph_vertex_list,startVertex)
        for vertex in graph_vertex_list:
            if vertex.color == 0:
                self.components = self.components + 1
                print("DFS Tree")
                self.print_dfs(dfs_list)
                print("Reverse DFS Tree")
                self.print_dfs(dfs_finish)
                dfs_finish.clear()
                dfs_list.clear()
                self.dfs(graph_vertex_list,vertex)

    def print_dfs(self,dfs_list):
        for vertex in dfs_list:
            print("Vertex: ",vertex.vertex, " StartTime: ",vertex.startTime, " FinishTime: ",vertex.finishTime)
        return

    def bfs(self,graph_vertex_list,startVertex):
        queue = deque([startVertex])
        startVertex.color = 1
        while len(queue)>0:
            vertex = queue.popleft()
            bfs_list.append(vertex)
            for node in vertex.adjacencyList.keys():
                if node.color == 0:
                    queue.append(node)
                    node.color = 1

    def driving_bfs(self,graph_vertex_list,startVertex):
        self.bfs(graph_vertex_list,startVertex)
        for vertex in graph_vertex_list:
            if vertex.color == 0:
                print("first time")
                print(bfs_list)
                print("BFS Tree")
                self.print_bfs(bfs_list)
                bfs_list.clear()
                self.bfs(graph_vertex_list,vertex)

    def print_bfs(self,bfs_list):
        for vertex in bfs_list:
            print("Vertex: ",vertex.vertex)
        return

    def getArticulationPoints(self,startVertex,count):
        print(startVertex.vertex,"ok")
        startVertex.low = self.artCount
        startVertex.depth = self.artCount
        self.artCount = self.artCount+1
        startVertex.color = 1
        for vertex in startVertex.adjacencyList.keys():
            if vertex.color == 0:
                self.getArticulationPoints(vertex,self.artCount)
            print()
            startVertex.low = min(startVertex.low,vertex.low)

            if vertex.low >= startVertex.depth:
                if startVertex not in self.root and len(startVertex.adjacencyList.keys()) >1:
                    print(startVertex.vertex+" is an Articulation Point")
                    self.articulationPoints.append(startVertex)




    def drivingArticulationPoints(self,graph_vertex_list,startVertex,count):
        self.getArticulationPoints(startVertex,count)

        for vertex in graph_vertex_list:
            if vertex.color == 0:
                self.getArticulationPoints(vertex,count)

    def drivingTopSort(self,graph_vertex_list,startVertex):
        self.topSort(startVertex)
        for vertex in graph_vertex_list:
            if vertex.color == 0:
                self.topSort(vertex)

        print(self.tStack[::-1])
        return

    def topSort(self,startVertex):

        startVertex.color = 1
        for vertex in startVertex.adjacencyList.keys():
            if vertex.color == 0:
                self.topSort(vertex)

        self.tStack.append(startVertex.vertex)


class GraphVertex:
    def __init__(self,vertex):
        self.vertex = vertex
        self.adjacencyList = collections.defaultdict(int)
        self.color = 0
        self.startTime = 0
        self.finishTime = 0
        self.parent = None
        self.low = 0
        self.depth = 0
        self.articulationPoint = False



def main():

    graph_vertex_list = []
    print("Enter the number of vertices")
    v = int(input())
    for i in range(0,v):
        print("Enter",i+1,"vertex")
        x = input()
        graph_vertex_list.append(GraphVertex(x))

    for i in range(0,v):
        print("Enter adjacency list for : ", graph_vertex_list[i].vertex)
        print("Enter number of edges for vertex : ",graph_vertex_list[i].vertex)
        e = int(input())

        for j in range(0,e):
            print("Enter Second vertex")
            y = input()
            print("Enter the weight of this edge")
            w = int(input())
            vertex = ord(y) - ord('a')
            graph_vertex_list[i].adjacencyList[graph_vertex_list[vertex]] = w

    graph = Graph()
    print("Enter the number vertex with which you want to find the dfs like a=0,b=1 etc")
    x = int(input())
    graph.driving_dfs(graph_vertex_list,graph_vertex_list[x])
    graph.components = graph.components+1
    print("DFS Tree")
    graph.print_dfs(dfs_list)
    print("Reverse DFS Tree")
    graph.print_dfs(dfs_finish)
    print("Total Number of components: ",graph.components)
    print("Ordering based on finished times")

    if graph.cycle:
        print("It has a cycle")
    else:
        print("No cycle")

    for vertex in graph_vertex_list:
        vertex.color = 0

    graph.driving_bfs(graph_vertex_list,graph_vertex_list[x])
    print("BFS Tree")
    graph.print_bfs(bfs_list)

    for vertex in graph_vertex_list:
        vertex.color = 0
    #graph.root.append(graph_vertex_list[x])
    #graph.drivingArticulationPoints(graph_vertex_list,graph_vertex_list[x],1)
    #for vertex in graph_vertex_list:
    #    print(vertex.depth,"d")
    #    print(vertex.low, "l")
    graph.drivingTopSort(graph_vertex_list,graph_vertex_list[x])
main()
