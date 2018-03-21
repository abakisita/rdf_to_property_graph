from database_mapper import database_mapper


if __name__ == "__main__":
    # sample data file
    data_file = '../data/sample_data.nt'
    namespace = "http://db.uwaterloo.ca/~galuc/wsdbm/"
    # Initialization
    database_mapper_ = database_mapper(data_file, namespace=namespace)
    # Mapping database
    database_mapper_.map_database()
    # Saving database
    database_mapper_.save_database('../data/graph.graphml')
