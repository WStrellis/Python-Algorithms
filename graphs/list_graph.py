class List_Graph:
    def __init__(self):
        self.vertices = {}

    def add_vert(self, value, connections=None):
        """Add a new vertex to the graph

        Arguments:
            value: any -- the vertex
            connections: set -- a set of values representing connections
        """
        if connections:
            # check that all connection verts are valid
            ok = self.validate_edges(connections)
            if not ok:
                raise ValueError(
                    f'Invalid connection. Node {c} does not exist in this graph.')
            self.vertices[value] = connections
        else:
            self.vertices[value] = set()

    def add_directed_edge(self, vert, new_connection):
        # check vertice
        if vert not in self.vertices:
            raise ValueError(f'Invalid node {vert}')
        # check new edge
        if new_connection not in self.vertices:
            raise ValueError(f'Invalid connection {new_connection}')
        self.vertices[vert].add(new_connection)

    def get_neighbors(self, vert):
        if vert in self.vertices:
            return self.vertices[vert]
        raise ValueError('Vertex does not exist')

    def validate_edges(self, connections):
        ok = True
        for c in connections:
            if not self.vertices.get(c):
            ok = False
            break
        return ok

    def bft(self, start_vert):
        #  create queue
        # enqueue start vertex
        # create set to store visited vertices
        # while queue is not empty
        # dequeue first vert
        # check if visited
        # if not visited
        # mark as visited
        # enque all neighbors

    def bfs(self, start, destination):
        #  create queue
        # enqueue A PATH to start vertex
        # create set to store visited vertices
        # while queue is not empty
        # dequeue first vert
        # get the vertex from the end of the path
        # check if visited
        # if not visited
        # check if it is the destination
        # if so ,return vertex
        # mark as visited
        # enque a path to all of its neighbors
        # enque the copy

    def dft(self, start_vert):
        #  create stack
        # push start vertex to stack
        # create set to store visited vertices
        # while stack is not empty
        # dequeue first vert
        # check if visited
        # if not visited
        # mark as visited
        # enque all neighbors
