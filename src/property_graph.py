from pygraphml import Graph
from pygraphml import GraphMLParser
from rdf_data_processor import rdf_file_processor

# Create graph

class Property_Graph:

    def __init__(self):

        self.g = Graph()
        self.vertex_id = 0
        self.edge_id = 0

    def add_vertex(self, label, value, property=None):

        for n in self.g._nodes:
            if n[label] == value:
                print "vertex already exists"
                return n
        node = self.g.add_node(str(self.vertex_id))
        node[label] = value
        if property != None:
            node[property[0]] = property[1]
        self.vertex_id += 1
        return node
    
    def add_edge(self, label, label_value1, label_value2, default_property, property=None):
        
        n1 = None
        n2 = None
        for n in self.g._nodes:
            if n[label] == label_value1:
                n1 = n
            if n[label] == label_value2:
                n2 = n
        
        if n1 == None and n2 ==None:
            return

        edge = self.g.add_edge(n1, n2, directed=True)
        edge['property'] = default_property
        edge['id'] = str(self.edge_id)
        if property != None:
            edge[property[0]] = edge[property[1]]
        self.edge_id += 1


    def add_vertices_and_edge(self, label, label_value1, label_value2, default_edge_property,\
         edge_property=None, vertex1_property=None, vertex2_property=None):

        n1 = self.add_vertex(label, label_value1, vertex1_property)
        n2 = self.add_vertex(label, label_value2, vertex2_property)
        edge = self.g.add_edge(n1, n2, directed=True)
        edge['label'] = default_edge_property
        edge['id'] = str(self.edge_id)
        self.edge_id += 1
        if edge_property != None:
            edge[edge_property[0]] = edge[edge_property[1]]

    def add_property(self, label, label_value, property, to_edge=False):

        if to_edge:
            pass
        else:
            for n in self.g._nodes:
                if n[label] == label_value:
                    n[property[0]] = property[1]
                    break 

    def save_graph(self, file_name):
        parser = GraphMLParser()
        parser.write(self.g, file_name)

if __name__ == "__main__":
    
    con = Property_Graph()
    con.add_vertex('URI', 'something_dot_com', ['name','myself'])
    con.add_vertex('URI', 'something1_dot_com', ['name','urself'])
    con.add_vertex('URI', 'something2_dot_com', ['name','herself'])
    con.add_vertex('URI', 'something3_dot_com', ['name','himself'])
    con.add_edge('URI','something_dot_com', 'something1_dot_com', 'knows')
    con.add_edge('URI','something1_dot_com', 'something2_dot_com', 'knows')
    con.save_graph("myGraph.graphml")


