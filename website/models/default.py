# -*- coding: utf-8 -*-
from website import bdd
import yaml 

class Education(object):
    """model parsing a yaml bdd concerning flevern's education"""
    
    def __init__(self, bdd):
        with open(bdd, 'r') as f:
            self.doc = yaml.load(f)
        pass
    
    def getbdd(self):
        return yaml.dump(self.doc)
        
    def getSchools(self):
        return self.doc["Schools"]
        
    def getSchoolsNames(self): 
        return (s["name"] for s in self.getSchools())
    
    def getSchoolByName(self, name):
        for s in self.getSchools():
            if s["name"] == name:
                return s
        return None
        
    def getProjects(self):
        return self.doc["Projects"]
        
    def getProjectsNames(self):
        return (p["name"] for p in self.getProjects())
        
    def getProjectByName(self, name):
        for p in self.getProjects():
            if p["name"] == name:
                return p
        return None
    
      
model = Education(bdd)