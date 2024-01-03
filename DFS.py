class Graph:

    def __init__(self):
        self.graph={}
    
    def add_edge(self,vertex,neighbour):
        if vertex not in self.graph:
            self.graph[vertex]=[]
        if neighbour not in self.graph:
            self.graph[neighbour]=[]
        
        #as its a unidirected graph, we add edge in both directions
        self.graph[vertex].append(neighbour)
        self.graph[neighbour].append(vertex)

def dfs(graph,start,visited):
    #graph: the graph as an adjacency list
    #start: the starting vertex
    #visited: keeping track of already visited vertices

    #first mark as visited, then traverse
    
    visited.add(start)
    print("visited: ",start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            #recursively call dfs for unvisited neighbors
            dfs(graph,neighbor,visited)

if __name__=="__main__":
    my_graph=Graph()
    my_graph.add_edge(1,2)
    my_graph.add_edge(1,3)
    my_graph.add_edge(2,4)
    my_graph.add_edge(2,5)
    my_graph.add_edge(3,6)

    visited_set=set()

    #choose arbitrary starting point
    start_vertex=1

    print("starting DFS from vertex",start_vertex)
    dfs(my_graph.graph,start_vertex,visited_set)



    
