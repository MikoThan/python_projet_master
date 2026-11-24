import Document

class ArxivDocument(Document.Document):
    def __init__(self, titre, date, auteur, url, texte, co_auteurs):
        super().__init__(titre, date, auteur, url, texte)
        self.co_auteurs = co_auteurs

    def getCoAuteurs(self):
        return self.co_auteurs
    
    def setCoAuteurs(self, co_auteurs):
        self.co_auteurs = co_auteurs

    def __str__(self):
        sortie = super().__str__()
        for auteur in self.co_auteurs:
            sortie += f"Co-Auteur : {auteur.name}"
        return sortie