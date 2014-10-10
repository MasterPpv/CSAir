'''
@author: Priten Vora
'''
from src.Graph import Graph
from src.Node import Node

def main():
    my_graph = Graph()
    node1 = Node({"Node 1 Data Piece 1" : 1, "Node 1 Data Piece 2" : 2})
    node2 = Node({"Node 2 Data Piece 1" : 3, "Node 2 Data Piece 2" : 4, "Node 2 Data Piece 3" : 5})
    node3 = Node({"Node 3 Data Piece 1" : 6})
    node4 = Node({"Node 4 Data Piece 1" : 7, "Node 4 Data Piece 2" : 8})
    my_graph.add_node(node1)
    my_graph.add_node(node2)
    my_graph.add_node(node3)
    my_graph.add_node(node4)
    my_graph.add_edge((node1, node2), 0.5)
    my_graph.add_edge((node1, node3), 0.25)
    my_graph.add_edge((node1, node4), 1.5)
    my_graph.add_edge((node2, node4), 1.2)
    my_graph.add_edge((node4, node1), 2.5)
    my_graph.add_edge((node4, node3), 1.8)
    print my_graph
    print my_graph.get_nodes()
    print my_graph.get_edges()
    all_nodes = my_graph.get_nodes()
    all_edges = my_graph.get_edges()
    for node_entry in all_nodes:
        print node_entry
        print node_entry.get_neighbors_in()
        print node_entry.get_neighbors_out()
        print node_entry.edges_in
        print node_entry.edges_out
        print node_entry.get_indegree()
        print node_entry.get_outdegree()
        print node_entry.get_degree()
        print node_entry.data
    for edge_entry in all_edges:
        print edge_entry
        print edge_entry.get_weight()

if __name__ == '__main__':
    main()