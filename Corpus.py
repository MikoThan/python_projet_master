class Corpus:
    def __init__(self, nom, authors, id2doc):
        self.nom = nom
        self.authors = authors
        self.id2doc = id2doc
        self.ndoc = len(authors)
        self.naut = len(id2doc)

    def __repr__(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

def singleton(cls):
    instances = [None]

    def wrapper(*args, **kwargs):
        if instances[0] is None:
                instances[0] = cls(*args, **kwargs)
        return instances[0]

    return wrapper

@singleton
class Zoo:
    def __init__(self, nom):
        self.nom = nom
        self.animaux = []

    def add_animal(self, animal):
        self.animaux.append(animal)

    def afficher_animaux(self):
        print(f"Animaux du zoo : {self.animaux}")
        for animal in self.animaux:
            print(f"- {animal}")

        
