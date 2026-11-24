import urllib.request
import urllib.parse
import xmltodict

theme = "climate"
docs = []
origines = []

url_arxiv = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
    {"search_query": "all:" + theme, "start": 0, "max_results": 50})
print(f"url_arxiv : {url_arxiv}")

with urllib.request.urlopen(url_arxiv) as reponse:
    d_arxiv = xmltodict.parse(reponse.read())

print(d_arxiv.keys())                # feed : la racine du document XML
print(f"arxiv keys feed : {d_arxiv['feed'].keys()}")        # title, id, updated, entry...


entrees = d_arxiv["feed"].get("entry", [])
if isinstance(entrees, dict):
    entrees = [entrees]
print(len(entrees))
print(entrees[0].keys())  
print(entrees[0]["author"])