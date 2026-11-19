
class HackerNewsDocument(Document):
    def __init__(self):
        super().__init__()


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
