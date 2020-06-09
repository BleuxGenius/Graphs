"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # creates a new vertex id adds to the dictionary
        # set() -> new empty set object set(iterable) -> new set object
        self.vertices[vertex_id] = set

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
           self.vertices[v1].add(v2)

            # add to the edge 
        else:
            print("Error adding edge, Vertex not found")   

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # if the vertex id is in the vertices dict 
        if vertex_id in self.vertices:
            # return the vertex Id
           return self.vertices[vertex_id]
        #     if not return none 
        else:
            return None   

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # create a queue and enqueue starting a vertex
        planned_visited = Queue()
        planned_visited.enqueue([starting_vertex])

        # create a set of traversed vertices
        visited_vertices = set()

        #  while the queue is not empty 
        while planned_visited.size() > 0:
            # dequeue/pop the first vertex on the queue
            current_vertex = planned_visited.dequeue()
            #  if current vertex is not visited
            if current_vertex not in visited_vertices:
                # print the vertex 
                print(current_vertex)
                #  mark as visited , add to visited vertices 
                visited_vertices.add(current_vertex)
                # add all unvisited neighbors to the queue 
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        planned_visited.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create planned_visited stack and add starting vertex
        print("DFT")
        planned_visited = Stack()
        planned_visited.push(starting_vertex)

        #  create set for visiting verticies 
        visited_vertices = set()
        #  while planned_visited is not empty
        while planned_visited.size() > 0:
            # pop the first vertex on the stack 
            current_vertex = planned_visited.pop()
            #  if vertex has not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
            # mark as visited, (add to visitied_vertices)
                visited_vertices.add(current_vertex)
            # add all unvisited neighbors to the stack 
            for neighbor in self.get_neighbors(current_vertex):
                if neighbor not in visited_vertices:
                    planned_visited.push(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
