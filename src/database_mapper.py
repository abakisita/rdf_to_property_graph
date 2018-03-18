from rdf_data_processor import rdf_data_processor
from property_graph import Property_Graph

def main():

    graph = Property_Graph()
    data_modality = rdf_data_processor('sample_data.nt')
    label = 'URI'
    while True:
        data = data_modality.process_line()

        if data == None:
            break
        database = data[0]
        vertex1_property = [label, database[0]]
        vertex2_property = [label, database[2]]
        edge_property = database[1]

        names = data[1]
        found_non_URI_field = data[2]
        if found_non_URI_field == False:
            graph.add_vertices_and_edge('name', names[0], names[1], edge_property, vertex1_property=vertex1_property, vertex2_property=vertex2_property)
        else:
            graph.add_property('name', names[0], [database[1], names[1]])
        '''
        for i in range(len(subjects)):
            subject = subjects[i]
            name = names[i]
            graph.add_vertex('name', name, property=[label, subject])
        '''
    graph.save_graph('graph.graphml')

main()
