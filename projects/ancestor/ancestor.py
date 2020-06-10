

# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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

    def get_ancestor(self, vertex_id):
    #  return children's parents
        return self.vertices[vertex_id]


graph = Graph()

def create_vertex(ancestors):
    # create the graph
    for ancestor in ancestors:
        #  create a tuple 
        ancestor_list = list(ancestor)
        # creating vertex in the list 
        graph.add_vertex(ancestor_list[0])
        graph.add_vertex(ancestor_list[1])


def create_edges(ancestors):
    # create the edges 
    for ancestor in ancestors:
        #  create the edge
        ancestor_list = list(ancestor)
        graph.add_edge(ancestor_list[1], ancestor_list[0]) 

def earliest_ancestor(ancestors, starting_node):
    # finding the shortest path from child to ancestor

    # helper functions for adding vertex and edges 
    create_vertex(ancestors)
    create_edges(ancestors)

    bfs_path = Queue()
    # enqueue path to starting word
    bfs_path.enqueue([starting_node])
    vistited_vertices = set()
    # while queue is not empty
    while bfs_path.size() > 0:
        # dequeue path
        current_path = bfs_path.dequeue()
        # get the ancestor from the path
        collected_ancestor = current_path[-1]
        # check if its been visited. if not 
        if collected_ancestor not in vistited_vertices:
            # mark it as visited
            vistited_vertices.add(collected_ancestor)
            # enqueue a path to each ancestor
            for neighbor in graph.get_ancestor(collected_ancestor):
                copied_path = current_path.copy()
                copied_path.append(neighbor)
                bfs_path.enqueue(copied_path)
                # if not in ancestors return -1
            if len(vistited_vertices) == 1:
                return -1
            else:
                return collected_ancestor
