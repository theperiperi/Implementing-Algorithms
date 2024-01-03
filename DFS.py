class Graph:
    def __init__(self):
        self.graph={}
    
    def add_edge(self,vertex,neighbor):
        #changing input to for of which and all vertices one vertice is connected to
        if vertex not in self.graph:
            self.graph[vertex]=[]
        if neighbor not in self.graph:
            self.graph[neighbor]=[]

        #add vertex in both directions because it is a uni-directed graph
        self.graph[vertex].append(neighbor)
        self.graph[neighbor].append(vertex)

def DFS(graph,start,visited):
    visited.add(start)
    print("visited ",start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph,neighbor,visited)

if __name__=="__main__":
    my_graph=Graph()
    my_graph.add_edge(1,3)
    my_graph.add_edge(1,2)
    my_graph.add_edge(2,4)
    my_graph.add_edge(2,5)
    my_graph.add_edge(3,6)

    visited_set=set()
    start_vertex=1

    print("Starting DFS from vertex",start_vertex)
    DFS(my_graph.graph,start_vertex,visited_set)
    
    