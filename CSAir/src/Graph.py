'''
@author: Priten Vora
'''
from Edge import Edge
from Node import Node
import sys
from decimal import Decimal

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
            endpoint_1.edges_out.append(new_edge)
            endpoint_1.outdegree += 1
            endpoint_2.neighbors_in.append(endpoint_1)
            endpoint_2.edges_in.append(new_edge)
            endpoint_2.indegree += 1
        else:
            raise ValueError("Edge (%s, %s) is already in the graph." %(endpoint_1, endpoint_2))

    def delete_node(self, graph_node):
        return 1

    def delete_edge(self, graph_edge):
        return 1

    def get_shortest_edge(self):
        '''
        Figures out and returns the shortest edge in the
        graph (returns the actual Edge object, not its weight)
        '''
        shortest_edge_weight = sys.maxint
        shortest_edge = Edge((Node({}), Node({})), shortest_edge_weight)
        for current_edge in self.edge_list:
            if current_edge.get_weight() < Decimal(shortest_edge_weight):
                shortest_edge_weight = current_edge.get_weight()
                shortest_edge = current_edge
        return shortest_edge

    def get_longest_edge(self):
        '''
        Figures out and returns the longest edge in the
        graph (returns the actual Edge object, not its weight)
        '''
        longest_edge_weight = -sys.maxint - 1
        longest_edge = Edge((Node({}), Node({})), longest_edge_weight)
        for current_edge in self.edge_list:
            if current_edge.get_weight() > Decimal(longest_edge_weight):
                longest_edge_weight = current_edge.get_weight()
                longest_edge = current_edge
        return longest_edge

    def get_average_edge_weight(self):
        '''
        Calculates and returns the average weight of all of
        the edges currently in the graph
        '''
        num_edges = Decimal(len(self.edge_list))
        sum_weight = Decimal(0)
        for current_edge in self.edge_list:
            sum_weight += current_edge.get_weight()
        average = Decimal(sum_weight / num_edges)
        return average

    def get_hub_list(self):
        '''
        Gets a list of all of the nodes in the graph that have
        the highest degree. If there are multiple nodes with
        equal degree and that degree is the highest degree, both
        nodes will be included in the list that is returned.
        '''
        max_degree = -sys.maxint - 1
        hub_list = []
        for current_node in self.node_list:
            current_degree = current_node.get_degree()
            if current_degree == max_degree:
                hub_list.append(current_node)
            elif current_degree > max_degree:
                del hub_list[:]
                hub_list.append(current_node)
                max_degree = current_degree
        return hub_list