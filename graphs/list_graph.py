class List_Graph:
    def __init__(self):
        self.vertices = {}

    def add_vert(self, value, connections=None):
        """Add a new vertex to the graph

        Arguments:
            value: any -- the vertex
            connections: set -- a set of values representing connections
        """
        self.vertices[value] = connections if connections else set()

    def add_edge(self, vert, new_connection):
        self.vertices[vert].add(new_connection)
