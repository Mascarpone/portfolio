# -*- coding: utf-8 -*-
import os
import yaml 

from website import bdd



class Education(object):
    """ model parsing a yaml bdd concerning flevern's education """
    
    def __init__(self, bdd):
        self.doc = {}
        current_dir = os.path.dirname(os.path.realpath(__file__))
        bdd_path = os.path.join(current_dir, '..', '..', bdd)
        with open(bdd_path, 'r') as documents:
            for data in yaml.load_all(documents):
                self.doc[data["document"]] = data
        pass
    
    def getbdd(self):
        return yaml.dump(self.doc)
        
    def getSchools(self):
        return self.doc["schools"]["schools"]
        
    def getSchoolsNames(self): 
        return (s["name"] for s in self.getSchools())
    
    def getSchoolByName(self, name):
        for s in self.getSchools():
            if s["name"] == name:
                return s
        return None
        
    def getProjects(self):
        return self.doc["projects"]["projects"]
        
    def getProjectsNames(self):
        return (p["name"] for p in self.getProjects())
        
    def getProjectByName(self, name):
        for p in self.getProjects():
            if p["name"] == name:
                return p
        return None
        
    def getDocument(self, docname):
        return self.doc[docname]
      
model = Education(bdd)