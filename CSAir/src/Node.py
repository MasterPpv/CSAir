'''
@author: Priten Vora
'''

class Node(object):
    '''
    classdocs
    '''

    def __init__(self, node_data):
        '''
        Constructor
        Initializes a node without any incoming or outgoing neighbors or
        edges, with a indegree and outdegree of zero, and the data passed
        along to it for the node to hold

        @type node_data: Dictionary - A Python Dictionary containing the node's data
        @param node_data: Any relevant data about the node that it needs to store 
        '''
        self.neighbors_in = []
        self.neighbors_out = []
        self.edges_in = []
        self.edges_out = []
        self.indegree = 0
        self.outdegree = 0
        self.data = node_data


    def get_degree(self):
        '''
        Returns the total number of other nodes in the graph that this node is
        connected to, regardless of direction

        @rtype: int - A standard integer
        @return: The degree of this node irrespective of direction
        '''
        all_neighbors = self.neighbors_in + self.neighbors_out
        unique_neighbors = set()
        for neighbor in all_neighbors:
            unique_neighbors.add(neighbor)
        return len(unique_neighbors)

    def get_indegree(self):
        '''
        Returns the incoming degree of this node (how many external vertices
        have edges that lead to this node)

        @rtype: int - A standard integer
        @return: The incoming degree of this node
        '''
        return self.indegree

    def get_outdegree(self):
        '''
        Returns the outgoing degree of this node (how many edges there are that
        originate at this node and lead to other nodes in the graph)

        @rtype: int - A standard integer
        @return: The outgoing degree of this node
        '''
        return self.outdegree

    def get_neighbors_in(self):
        '''
        Returns a list of all the nodes in the graph that
        have edges that lead to this node

        @rtype: list - A standard Python list
        @return: A list of all nodes with edges leading to this node
        '''
        return self.neighbors_in

    def get_neighbors_out(self):
        '''
        Returns a list of all the nodes in the graph that
        have edges leading from this node to those nodes

        @rtype: list - A standard Python list
        @return: A list of all nodes that this node has edges to
        '''
        return self.neighbors_out

    def get_adjacents(self):
        '''
        Returns a list of all the nodes in the graph that
        are adjacent to the given node - includes all nodes
        that are incoming AND outgoing neighbors for this node

        @rtype: list - A standard Python list
        @return: A list of all nodes adjacent to the given node
        '''
        adjacents = []
        for entry in self.neighbors_in:
            if not entry in adjacents:
                adjacents.append(entry)
        for entry in self.neighbors_out:
            if not entry in adjacents:
                adjacents.append(entry)
        return adjacents