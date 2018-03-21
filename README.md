# rdf_to_property_graph
Library to map RDF data to Property Graph Model data.

This library provides *class database_mappper* to convert ntripple files to property graph model data. 

## Dependencies: 
1. pygraphml (A simple library for handelling graph databases in python.

    ### Documentation
    Official document can be found at

        http://hadim.fr/pygraphml/overview.html 

    ### Installation 
    Use following command for pip installation. 

        pip install pygraphml

    It can be installed inside a virtual environment. See the official documentation.

## API of class database_mapper

1. *class* database_mapper(*string* input_file, *string* namespace)
    
    input_file : ntriple (.nt) input_file path
     
    namespace is a *optional* arguement representing namespace of URI. It is only used to extract names of the entities. These Extracted names are used as key values of key 'names' which are nescessary to uniquely identify a vertex. 
    Example of namespace: 'http://db.uwaterloo.ca/~galuc/wsdbm/'

2. *database_mapper*.map_database()

    Maps given RDF database to Property Graph Model. 

3. *database_mapper*.save_database(*string* output_file_name)

    output_file_name : File to store mapped database (a *.graphml* file e.g. output.graphml)


## Exapmle : 

    Use of the library can be illustrated with provided example.

    To run exapmle script go to eaxmple directory and run following command in command line,

        python example.py