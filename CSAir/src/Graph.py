'''
@author: Priten Vora
'''

class Graph(object):
    '''
    classdocs
    '''

    # Whether the graph is a directed graph or not
    DIRECTED = True

    def __init__(self):
        '''
        Constructor
        Initializes an empty graph with no neighbors
        '''
        # No neighbors at first
        self.neighbor_nodes = {}
        self.incident_edges = {}

    def get_nodes(self):
        '''
        Returns a list of all of the nodes in the graph
        
        @rtype: list - A standard Python list
        @return: A list of all nodes currently in the graph
        '''
        return list(self.neighbor_nodes.keys())

    def get_neighbors(self, graph_node):
        '''
        Returns a list of all the nodes in the graph that
        are adjacent to the given node

        @type graph_node: node - A single node in a graph
        @param graph_node: A single node that already exists in this graph

        @rtype: list - A standard Python list
        @return: A list of all nodes adjacent to the given node
        '''
        return list(self.neighbor_nodes[graph_node])

    def get_edges(self):
        '''
        Returns a list of all the edges in the graph

        @rtype: list - A standard Python list
        @return: A list of all edges currently in the graph
        '''
        edge_list = []
        '''
        Goes through each neighbor in each node's list of neighbors
        and adds every pair to the list of edges to return
        '''
        for current_node, current_neighbor_list in self.neighbor_nodes.items():
            for current_neighbor in current_neighbor_list:
                edge_list.append((current_node, current_neighbor))
        return edge_list

    def get_incidents(self, graph_edge):
        '''
        Returns a list of all the edges in the graph that
        are incident to the given edge
        
        @type graph_edge: edge - A single edge in a graph
        @param graph_edge: A single edge that already exists in this graph

        @rtype: list - A standard Python list
        @return: A list of all edges incident to the given edge
        '''
        return list(self.incident_edges[graph_edge])

    def add_node(self, graph_node):
        '''
        Adds a new node to the graph without any connections to
        any other nodes in the graph

        @type graph_node: node - A single node to be added to the graph
        @param graph_node: A node to be added to the graph that isn't in it already
        '''
        if graph_node not in self.neighbor_nodes:
            self.neighbor_nodes[graph_node] = [] 
            self.incident_edges[graph_node] = []

    def add_edge(self, graph_edge):
        '''
        Adds a new edge to the graph connecting two nodes. Must be given
        as a standard Python tuple, with the starting vertex as the first
        element of the tuple, and the ending vertex as the second.

        @type graph_node: node - A single node to be added to the graph
        @param graph_node: A node to be added to the graph that isn't in it already
        '''
        return 1
    def delete_node(self, graph_node):
        return 1
    def delete_edge(self, graph_edge):
        return 1