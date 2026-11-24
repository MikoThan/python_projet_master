class Document:

    def __init__(self, titre, date, auteur, url, texte):
        self.titre = titre
        self.date = date
        self.auteur = auteur
        self.url = url
        self.texte = texte

    def __str__(self):
        sortie = f"{self.titre} de {self.auteur}"
        sortie += {self.texte}
        return sortie