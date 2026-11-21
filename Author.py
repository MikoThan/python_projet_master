class Author:
    def __init__(self, nom, nbdoc):
        self.name = nom
        self.ndoc = nbdoc
        self.production = {}

    def add(self, titre, document):
        self.production[titre] = document

    def __str__(self):
        return f"Nom : {self.name}, nombre de documents : {self.ndoc}, Documents écrits : {self.production}"


