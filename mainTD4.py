import Document
import Author

import json
import html
import urllib.request
import urllib.parse
import xmltodict
import pandas as pd

theme = "climate"
docs = []
origines = []

url_hn = "https://hn.algolia.com/api/v1/search?" + urllib.parse.urlencode(
    {"query": theme, "tags": "story", "hitsPerPage": 50})

with urllib.request.urlopen(url_hn) as reponse:
    d_hn = json.load(reponse)

hits = d_hn["hits"]

id2aut = {}
for hit in hits:
    nom_auteur = hit.get("author")
    if nom_auteur not in id2aut:
        id2aut[nom_auteur] = Author.Author(nom_auteur, 0)
    id2aut[nom_auteur].ndoc += 1
    
for auteur in id2aut.values():
    print(auteur)
    
#TODO finir les stats