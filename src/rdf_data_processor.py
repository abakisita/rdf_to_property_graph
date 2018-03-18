import numpy as np 
import re

class rdf_data_processor:

    def __init__(self, file):
        
        self.name_space = "http://db.uwaterloo.ca/~galuc/wsdbm/"
        self.subject_library = ['AgeGroup', 'City', 'Country', 'Gender', 'Genre', 'Language', 'Offer', 'Product',\
         'ProductCategory', 'Purchase', 'Retailer', 'Review', 'Role', 'SubGenre', 'Topic', 'User', 'Website']
        self.file = file
        self.f = open(file)

    def read_line(self):
        line = self.f.readline()
        if line == '':
            return None
        return line

    def process_line(self):

        # read next line
        line = self.read_line()
        if line == None:
            return None
        # remove leading whitespaces if any
        line = line.lstrip()
        
        # if the entity is URI or not
        found_non_URI_field = False

        words = line.split()
        for i in range(len(words)):
            words[i] = re.sub("<", "", words[i])
            words[i] = re.sub('>', "", words[i])
            length = len(words[i])
            words[i] = re.sub('"', "", words[i])
            if length != len(words[i]):
                print words[i]
                found_non_URI_field = True
        
        names = []
        subject = words[0]
        obj = words[2]
        name = re.sub(self.name_space, "", subject)
        names.append(name)
        name = re.sub(self.name_space, "", obj)
        names.append(name)
        return words, names, found_non_URI_field

"""
Test code 
Load sample fileand extract information form each line
"""
if __name__ == "__main__":
    file_processor = modadility_file_processor("saved.txt")
    w = file_processor.process_line()
    an_w = file_processor.process_line()

    print w, an_w