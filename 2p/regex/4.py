from urllib import request
from bs4 import BeautifulSoup
import nltk
import json

hdr = {
    'User-Agent': 'Wget/1.13.4 (linux-gnu)',
    'Accept': '*/*'
}

noticia = "https://www.elmundo.es/deportes/futbol/champions-league/2024/04/15/661d6027e4d4d8710a8b4598.html"

req = request.Request(noticia, headers=hdr)
response = request.urlopen(req)

data = BeautifulSoup(response, 'html.parser')
# print(data.prettify())

print("\nEncabezado")
print(data.title.text)
p = data.find_all("article", {"class": "ue-c-article"})
print("\nCuerpo")
for i in p:
    print(i.text)
