import json
import Document

class Corpus:
    def __init__(self, nom, authors={}, id2doc={}):
        self.nom = nom
        self.authors = authors
        self.id2doc = id2doc
        self.ndoc = len(self.id2doc)
        self.naut = len(self.authors)

    def tri_dico(self):
        nouv_dict = dict(sorted(self.id2doc.items(), key=lambda item: item[1].date)) #tri selon la clé date des objets documents
        return nouv_dict

    def __repr__(self):
        dico_trie = self.tri_dico()
        for document in dico_trie.values():
            print(f"{document.date} - {document.titre}")

    def save(self): #TODO peut etre à modif avec les classes filles de document
        data = {
            "nom": self.nom,
            "id2doc" : {
                str(identifiant): {
                    "titre": doc.titre,
                    "date": doc.date,
                    "auteur": doc.auteur,
                    "url": doc.url,
                    "texte": doc.texte
                }
                for identifiant, doc in self.id2doc.items()
            },
        }
        with open(f"{self.nom}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, fichier): #TODO peut etre à modif avec les classes filles de document
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(fichier)
            self/nom = data["nom"]
            self.id2doc = {
                identifiant: Document.Document(**champs)
                for identifiant, champs in data["id2doc"].items()
            }
            self.authors = {} #pas de dico d'auteurs sauvegardés dans le fichier
            self.ndoc = len(self.id2doc)
            self.naut = len(self.authors)#pas de taille


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

        
