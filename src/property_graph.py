"""
This class implements property graph model and required functionalities to 
create property graph models.
It uses pygraphml library for underlying graph implementation.

Methods:

    1. add_vertex() : adds a vertex to the graph. If the vertex with same name already exists,
        it returns the existing vertex.

    2. add_edge() : adds edge between two vetices of graph

    3. add_vertices_and_edge() : adds two vertices and edge connecting them

 """

from pygraphml import Graph
from pygraphml import GraphMLParser
from rdf_data_processor import rdf_data_processor

class Property_Graph:

    def __init__(self):
        
        """
        Initializes graph parameters.
        """
        self.g = Graph()
        self.vertex_id = 0
        self.edge_id = 0

    def add_vertex(self, label, value, property=None):

        """
        Adds a vertex to the graph.

        @param label: default label or key by which vertex is to be 
            added (vertex will be uniquely by this label and its value) e.g. "name"
        @param value: value of above label e.g. "product0012"
        @param property: list of length 2 containing key name of property as first element
            and value of property as second element
        """
        
        # check if node with same label already exists, if it does then return that node instance 
        for n in self.g._nodes:
            if n[label] == value:
                return n
        
        # add new node to graph
        node = self.g.add_node(str(self.vertex_id))
        # add default label and its value
        node[label] = value
        # add additional properties if provided
        if property != None:
            node[property[0]] = property[1]
        self.vertex_id += 1
        return node
    
    def add_edge(self, label, label_value1, label_value2, default_property, property=None):
        
        """
        Adds edge between two vertices.

        @param label: label or key value by which vertex will be searched e.g. "name" or "URI"
        @param label_value1 : value of above label or key of source vertex
        @param label_value2 : value of above label or key of target vertex
        @param default_property : default_property of edge (predicate in RDF terms)
        @param property : additional property, list of length 2 containing key name of property 
            as first element and value of property as second element
        """
        n1 = None
        n2 = None

        # Search source and target nodes
        for n in self.g._nodes:
            if n[label] == label_value1:
                n1 = n
            if n[label] == label_value2:
                n2 = n
        
        # If source or target doesn't exists, then return
        if n1 == None or n2 ==None:
            return

        # Add edge
        edge = self.g.add_edge(n1, n2, directed=True)
        # Add edge default property 
        edge['property'] = default_property
        edge['id'] = str(self.edge_id)
        # Add additional property if provided
        if property != None:
            edge[property[0]] = edge[property[1]]
        self.edge_id += 1


    def add_vertices_and_edge(self, label, label_value1, label_value2, default_edge_property,\
         edge_property=None, vertex1_property=None, vertex2_property=None):

        """
        Adds two vertices and edge connecting them

        @param label: default label or key by which vertex is to be 
            added (vertex will be uniquely by this label and its value) e.g. "name"
        @param label_value1 : value of above label or key of source vertex
        @param label_value2 : value of above label or key of target vertex
        @param default_edge_property : default_property of edge (predicate in RDF terms)
        @param edge_property : additional property, list of length 2 containing key name of property 
            as first element and value of property as second element
        @param vertex1_property: list of length 2 containing key name of property as first element
            and value of property as second element
        @param vertex2_property: list of length 2 containing key name of property as first element
            and value of property as second element
        """
        n1 = self.add_vertex(label, label_value1, vertex1_property)
        n2 = self.add_vertex(label, label_value2, vertex2_property)
        edge = self.g.add_edge(n1, n2, directed=True)
        edge['label'] = default_edge_property
        edge['id'] = str(self.edge_id)
        self.edge_id += 1
        if edge_property != None:
            edge[edge_property[0]] = edge[edge_property[1]]

    def add_property(self, label, label_value, property, to_edge=False):

        """
        Adds property to a edge or vertex 
        
        @param label : label or key by which desired edge or vertex will be searched
        @param label_value : value of above label or key
        @param property : property to be added, list of length 2 containing key name of 
            property as first element and value of property as second element
        @param to_edge : If set True, property will be added to edge, default value is False. 
        """
        if to_edge:
            # Yet to be implemented
            pass
        else:

            for n in self.g._nodes:
                if n[label] == label_value:
                    n[property[0]] = property[1]
                    break 

    def save_graph(self, file_name):

        """
        Save graph to .graphml file

        @param file_name : name of the file to which graph will be saved
        """
        parser = GraphMLParser()
        parser.write(self.g, file_name)


"""
Test code
"""
if __name__ == "__main__":
    
    con = Property_Graph()
    con.add_vertex('URI', 'something_dot_com', ['name','myself'])
    con.add_vertex('URI', 'something1_dot_com', ['name','urself'])
    con.add_vertex('URI', 'something2_dot_com', ['name','herself'])
    con.add_vertex('URI', 'something3_dot_com', ['name','himself'])
    con.add_edge('URI','something_dot_com', 'something1_dot_com', 'knows')
    con.add_edge('URI','something1_dot_com', 'something2_dot_com', 'knows')
    con.save_graph("test_output.graphml")


