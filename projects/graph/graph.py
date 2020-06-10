"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    #  a collection of data , represented by nodes and connections between nodes
    # trees are graphs 

    # nodes/vertices represent objects in data set 
    # edges - are the connections between the vertices/nodes 
    # typically optional // not all edges are created equally 
    # weight - cost to travel across an edge 

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # create new dict
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # creates a new vertex id to add to the dictionary
        # set() -> new empty set object set(iterable) -> new set object
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Adjacency List =>
        # complexity is 0(1)
        # constant time operations 
        # check if they exists
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

# time complexity O(V+E) where V is the number of vertices and E is the number of edges in the graph
# space complexity O(V) since an extra visited array is needed of size V

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

# function to call itself/ recursion ends when the condition is not greater than 0 

#  Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node and explores as far as possible along each branch before backtracking
 
    def dft_recursive(self, starting_vertex, visited_vertices = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
    # inital 
        if visited_vertices is None:
            visited_vertices = set()

        # track visited vertices 
        visited_vertices.add(starting_vertex)
        print(starting_vertex)    

        # call function recursively on the neighbors that were not visited 
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited_vertices:
                self.dft_recursive(neighbor, visited_vertices)


     
# breadth-first- search 
# A breadth-first search is when you search through vertexes in breadth-first order until you find the target vertex. A breadth-first search usually returns the shortest path from the starting vertex to the target vertex once the target is found.
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        bfs_path = Queue()
        bfs_path.enqueue([starting_vertex])

        # create set with traversed vertices
        visited_vertices = set()

        # while the queue is not empty
        while bfs_path.size() > 0:
            # dequeue/pop the first vertex
            current_path = bfs_path.dequeue()
            #  if not visited 
            if current_path[-1] not in visited_vertices:
                #  if the last added current path is not equal to the destionation vertex then return the current path 
                if current_path[-1] == destination_vertex:
                    # return the current path 
                    return current_path
                    # mark as visited 
                visited_vertices.add(current_path[-1])
                    # enqueue all neighbors (adding the element to the Queue)
                for next_vertices in self.get_neighbors(current_path[-1]):
                        new_path = list(current_path)
                        new_path.append(next_vertices)
                        bfs_path.enqueue(new_path)

# depth first search 
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print("dfs")
        # create an empty stack 
        dfs_path = Stack()
        #  path to sart the vertex 
        dfs_path.push([starting_vertex])
        # set for visitied vertices 
        visited_vertices = set()
        # while path is not empty
        while dfs_path.size() > 0:
            # pop the first vertex 
            current_path = dfs_path.pop()
            #  if not visited 
            if current_path[-1] not in visited_vertices:
                if current_path[-1] == destination_vertex:
                    return current_path
                    #  mark as visited
                visited_vertices.add(current_path[-1])
                # enqueue all neighbors 
                for next_vertices in self.get_neighbors(current_path[-1]):
                    new_path = list(current_path)
                    new_path.append(next_vertices)
                    dfs_path.push(new_path)

# Since DFS will pursue leads in the graph as far as it can, and then “back up” to an earlier branch point to explore that way, recursion is a good approach to help “remember” where we left off.
    def dfs_recursive(self, starting_vertex, destination_vertex, visited_vertices = None, current_path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initial 
        if visited_vertices is None:
            # created set object, items are unordered and will appear in randomized order
            visited_vertices = set()
            if current_path is None:
                current_path = []

                # track the visited vertex
                visited_vertices.add(starting_vertex)
                current_path = current_path + [starting_vertex]

                if starting_vertex == destination_vertex:
                    return current_path

                    # call the function recursively - on neighbors not visited 
                for neighbor in self.vertices[starting_vertex]:
                    if neighbor not in visited_vertices:
                        neighbor_path = self.dfs_recursive(neighbor, destination_vertex,visited_vertices,current_path)    
                        if neighbor_path:
                            return neighbor_path

        

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
