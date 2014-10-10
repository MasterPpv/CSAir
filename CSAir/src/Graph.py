'''
@author: Priten Vora
'''
from src.Edge import Edge
#from src.Node import Node

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
        # No nodes or edges at first

        self.node_list = []
        self.edge_list = []

    def get_nodes(self):
        '''
        Returns a list of all of the nodes in the graph
        
        @rtype: list - A standard Python list
        @return: A list of all nodes currently in the graph
        '''
        #return list(self.neighbor_nodes.keys())
        return self.node_list

    def get_edges(self):
        '''
        Returns a list of all the edges in the graph

        @rtype: list - A standard Python list
        @return: A list of all edges currently in the graph
        '''
        return self.edge_list


    def add_node(self, graph_node):
        '''
        Adds a new node to the graph without any connections to
        any other nodes in the graph

        @type graph_node: node - A single node to be added to the graph
        @param graph_node: A node to be added to the graph that isn't in it already

        @type node_data: Dictionary - A Python Dictionary containing the node's data
        @param node_data: Any relevant data about the node that it needs to store
        '''
        if not graph_node in self.node_list:
            self.node_list.append(graph_node)

    def add_edge(self, edge_vertices, edge_weight):
        '''
        Adds a new edge to the graph connecting two nodes. Must be given
        as a standard Python tuple, with the starting vertex as the first
        element of the tuple, and the ending vertex as the second. The
        nodes must be ones that do not already have an edge connecting
        them to each other. The edge's weight, if applicable, will also
        be stored, along with any other relevant data.

        @type edge_vertices: Tuple - A Tuple of the vertices that are the edge's endpoints
        @param edge_vertices: A Python Tuple containing two existing, unconnected graph nodes

        @type edge_weight: Decimal - A Python Decimal representing the edge's weight 
        @param edge_weight: The weight of the new edge (if applicable)
        '''
        endpoint_1, endpoint_2 = edge_vertices
        for endpoint in [endpoint_1, endpoint_2]:
            if not endpoint in self.node_list:
                raise ValueError("%s is missing from the current list of existing nodes." %endpoint)
        if not edge_vertices in self.edge_list:
            new_edge = Edge(edge_vertices, edge_weight)
            self.edge_list.append(new_edge)
            endpoint_1.neighbors_out.append(endpoint_2)
            endpoint_1.edges_out.append(edge_vertices)
            endpoint_1.outdegree += 1
            endpoint_2.neighbors_in.append(endpoint_1)
            endpoint_2.edges_in.append(edge_vertices)
            endpoint_2.indegree += 1
        else:
            raise ValueError("Edge (%s, %s) is already in the graph." %(endpoint_1, endpoint_2))

    def delete_node(self, graph_node):
        return 1

    def delete_edge(self, graph_edge):
        return 1