import Document

class HackerNewsDocument(Document.Document):
    def __init__(self, titre, date, auteur, url, texte, num_comments, children, points):
        super().__init__(titre, date, auteur, url, texte)
        self.num_comments = num_comments
        self.children = children
        self.points = points

    def getNumComments(self):
        return self.num_comments

    def setNumComments(self, num_comments):
        self.num_comments = num_comments

    def getChildren(self):
        return self.children
    
    def setChildren(self, children):
        self.children = children

    def getPoints(self):
        return self.points
    
    def setPoints(self, points):
        self.points = points

    def __str__(self):
        sortie = super().__str__()
        sortie += f"Nombre de commentaires : {self.num_comments}"
        sortie += f"Enfants : {self.children}"
        sortie += f"Nombre de points : {self.points}"
        return sortie

class Animal:
    type_animal = "animal"
    def __init__(self, nom, poids, age):
        self.nom = nom
        self.age = age
        self.poids = poids

    def __str__(self):
        return self.nom+str(self.age)+str(self.poids)

class Chien(Animal):
    type_animal = "chien"
    def __init__(self, nom, poids, age, race):
        super().__init__(nom, poids, age)
        self.race = race

    def __str__(self):
        return super().__str__()+self.race

c = Chien("Tokyo", 12, 12, "Tekkel")
print(c)

class AnimalGenerator:

    @staticmethod
    def factory(type_animal, nom, poids, age, **kwargs):
        if type_animal=="chien":
            return Chien(nom, poids, age, kwargs["race"])
