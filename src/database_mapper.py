"""
Class uses rdf_data_processor and property_graph classes to map 
RDF (ntriple) data to Property graph model data

Methods : 
    1. map_database() : Maps RDF data to Property graph model data.

    2. save_database() : Saves mapped database to .graphml file.
    
"""
from rdf_data_processor import rdf_data_processor
from property_graph import Property_Graph

class database_mapper(object):

    def __init__(self, input_file, namespace=''):
        """
        Initialization
        @param input_file : Input RDF (.nt) data file 
        @param namespace : Namespace to extract names of entities.
        """
        # Initialize graph 
        self.graph = Property_Graph()
    
        self.rdf_data_processor_ = rdf_data_processor(input_file, namespace=namespace)
        
        # default label or key for vertex (here it is URI as sample RDF data provided has data 
        #  in the form of URI's)
        self.label = 'URI'
    
    def map_database(self):

        """
        Maps RDF data to Property graph model data. 
        """
        while True:
            data = self.rdf_data_processor_.process_line()
            # check if data is None, (it is None at the end of file)
            if data == None:
                break
            rdf_data = data[0]
            # subject and object in RDF data will be vertices in property graph model 
            vertex1_property = [self.label, rdf_data[0]]
            vertex2_property = [self.label, rdf_data[2]]
            # predicate will be edge property connecting two verices
            edge_property = rdf_data[1]
            names = data[1]
            found_non_URI_field = data[2]
            # non-URI object in rdf data will be assigned as property of subject in graph data
            # for demonstration purpose, only non-URI objects are assigned as properties
            # this situation can be extended to any type of objects, e.g. object which is a country
            if found_non_URI_field == False:
                self.graph.add_vertices_and_edge('name', names[0], names[1], edge_property, \
                    vertex1_property=vertex1_property, vertex2_property=vertex2_property)
            else:
                self.graph.add_property('name', names[0], [rdf_data[1], names[1]])
        
    def save_database(self, output_file_name):
        
        self.graph.save_graph(output_file_name)


if __name__ == "__main__":
    data_file = 'sample_data.nt'
    namespace = "http://db.uwaterloo.ca/~galuc/wsdbm/"
    database_mapper_ = database_mapper(data_file, namespace=namespace)
    database_mapper_.map_database()
    database_mapper_.save_database('graph.graphml')
