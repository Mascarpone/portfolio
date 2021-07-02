import os
import yaml

from website import data_filename


class Data:
    def __init__(self, data_filename):
        self.doc = {}
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(current_dir, "..", "..", data_filename)
        with open(path, "r") as documents:
            for data in yaml.safe_load_all(documents):
                self.doc[data["document"]] = data

    def get_schools(self):
        return self.doc["schools"]["schools"]

    def get_projects(self):
        return self.doc["projects"]["projects"]

    def get_document(self, docname):
        return self.doc.get(docname)


model = Data(data_filename)
