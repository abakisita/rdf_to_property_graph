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
        
        names = []
        # first word in the line is subject
        subject = words[0]
        # second word in the line is predicate
        predicate = words[1]
        # third word in the line is object
        obj = words[2]
        # remove namespaces from subject and object to get names
        # if namespace is not provided, names will be same as subject and object 
        name = re.sub(self.namespace, "", subject)
        names.append(name)
        name = re.sub(self.namespace, "", obj)
        names.append(name)
        return [subject, predicate, obj], names, found_non_URI_field

