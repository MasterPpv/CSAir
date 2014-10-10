'''
@author: Priten Vora
'''

class Edge(object):
    '''
    classdocs
    '''


    def __init__(self, vertices_tuple, edge_weight):
        '''
        Constructor
        Given two nodes as a Tuple, initializes an edge
        connecting the two. Also goes through all other
        neighbors that each of the vertices already has
        and basically figures out what edges in the graph
        are incident to itself.

        
        '''
        self.endpoints = vertices_tuple
        self.incidents = []
        endpoint_1, endpoint_2 = vertices_tuple
        for endpoint in [endpoint_1, endpoint_2]:
            endpoint_connections = endpoint.edges_out
            for connection in endpoint_connections:
                if connection not in self.incidents:
                    self.incidents.append(connection)
        self.weight = edge_weight

    def get_weight(self):
        '''
        Returns the weight of this edge in the graph

        @rtype: Decimal - A standard Python Decimal
        @return: The weight of this edge
        '''
        return self.weight

    def get_endpoints(self):
        '''
        '''
        return self.endpoints

    def get_incidents(self, graph_edge):
        '''
        Returns a list of all the edges in the graph that
        are incident to the given edge
        
        @type graph_edge: edge - A single edge in a graph
        @param graph_edge: A single edge that already exists in this graph

        @rtype: list - A standard Python list
        @return: A list of all edges incident to the given edge
        '''
        return self.incidents