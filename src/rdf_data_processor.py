"""
This class implements the funcions required for processing RDF data (currently only ntriple files).
It takes ntripple file as input.
Methods:
    1. read_line() : Returns next line from the file. Returns None at the end of file.

    2. process_line() : Returns subject, predicate, object and names of subject and object
        It also returns "found_non_URI_field" flag.  
"""


import numpy as np 
import re
import urlparse

class rdf_data_processor:

    def __init__(self, file, namespace=''):
        """
        Initializing.
        @param file : Ntriple (.nt) file 
        @param namespace : Namespace to extract names of entities. 
        """
        self.namespace = namespace
        self.file = file
        print("Opening data file")
        self.f = open(file)

    def read_line(self):
        """
        Returns next line from the file. Returns None at the end of file.
        """
        line = self.f.readline()
        if line == '':
            return None
        return line

    def process_line(self):
        """
        Returns subject, predicate, object and names of subject and object
        It also returns "found_non_URI_field" flag.
        """
        # read next line
        line = self.read_line()
        if line == None:
            return None
        # remove leading whitespaces if any
        line = line.lstrip()
        found_non_URI_field = False
        # split line into words
        words = line.split()
        index_of_non_URI_fields = []
        for i in range(len(words)):
            # remove '<' and '>'
            words[i] = re.sub("<", "", words[i])
            words[i] = re.sub('>', "", words[i])
            length = len(words[i])
            # remove quotes ('"")
            words[i] = re.sub('"', "", words[i])
            # check if field is non-URI by checking the length before removing quotes is same or not
            # non-URI if length changes   
            if length != len(words[i]):
                found_non_URI_field = True
                index_of_non_URI_fields.append(i)

        names = [] 
        types = []
        # second word in the line is predicate
        predicate = urlparse.urlparse(words[1])
        if predicate.fragment == '':
            path = predicate.path[::-1]
            index = path.find('/')
            prop = path[0:index]
            prop = prop[::-1]
        else:
            prop = predicate.fragment    
        # first word in the line is subject
        subject = words[0]
        # third word in the line is object
        obj = words[2]
        # remove namespaces from subject and object to get names
        
        # removing namespace from subject 
        if 0 in index_of_non_URI_fields:
            pass
        else:
            subject_data = urlparse.urlparse(subject)
            if subject_data.fragment == '':
                path = subject_data.path[::-1]
                index = path.find('/')
                name = path[0:index]
                name = name[::-1]
                ty = ''.join(i for i in name if not i.isdigit())
            else:
                name = subject_data.fragment
                ty = name

        names.append(name)
        types.append(ty)
        # removing namespace from object 
        
        if 2 in index_of_non_URI_fields:
            name = obj
            ty = name
            pass
        else:
            obejct_data = urlparse.urlparse(obj)
            if obejct_data.fragment == '':
                path = obejct_data.path[::-1]
                index = path.find('/')
                name = path[0:index]
                name = name[::-1]
                ty = ''.join(i for i in name if not i.isdigit())
            else:
                name = obejct_data.fragment
                ty = name
        
        names.append(name)
        types.append(ty)
        return [subject, prop, obj], names, types, found_non_URI_field

if __name__ == "__main__":
    uri = "http://db.uwaterloo.ca/~galuc/wsdbm/Product10242"
    res = urlparse.urlparse(uri)
    path = res.path
    path = path[::-1]
    index = path.find('/')
    name = path[0:index]
    print path, index, name[::-1]
