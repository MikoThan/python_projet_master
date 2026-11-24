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
    #récupération du nom des auteurs
    nom_auteur = hit.get("author")
    if nom_auteur not in id2aut:
        id2aut[nom_auteur] = Author.Author(nom_auteur, 0)
    id2aut[nom_auteur].ndoc += 1

    #récupération des documents Hacker News
    texte = hit.get("story_text")
    num_comments = hit.get("num_comments")
    if not texte:
        texte = hit.get("title", "")
    texte = html.unescape(texte).replace("<p>", " ").strip()
    docs.append(texte)
    origines.append("hackernews")

#print("Documents Hacker News :", docs)
#TODO finir les stats

hits_avec_texte = [hit for hit in hits if hit.get("story_text")]

if hits_avec_texte:
    attributs_communs = set.intersection(
        *(set(hit.keys()) for hit in hits_avec_texte)
    )
else:
    attributs_communs = set()

print(sorted(attributs_communs))
    
"""for auteur in id2aut.values():
    print(auteur)"""

    