# -*- coding: utf-8 -*-
from website import bdd
import yaml 

class Education(object):
    """ model parsing a yaml bdd concerning flevern's education """
    
    def __init__(self, bdd):
        self.doc = {}
        with open(bdd, 'r') as documents:
            for data in yaml.load_all(documents):
                self.doc[data["document"]] = data
        pass
    
    def getbdd(self):
        return yaml.dump(self.doc)
        
    def getSchools(self):
        return self.doc["schools"]["Schools"]
        
    def getSchoolsNames(self): 
        return (s["name"] for s in self.getSchools())
    
    def getSchoolByName(self, name):
        for s in self.getSchools():
            if s["name"] == name:
                return s
        return None
        
    def getProjects(self):
        return self.doc["projects"]["Projects"]
        
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