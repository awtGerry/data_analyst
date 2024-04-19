from urllib import request
from bs4 import BeautifulSoup
import nltk
import json

hdr = {
    'User-Agent': 'Wget/1.13.4 (linux-gnu)',
    'Accept': '*/*'
}

noticia = "https://www.marca.com/futbol/premier-league/2024/04/15/661d120f46163f4abf8b4593.html"

req = request.Request(noticia, headers=hdr)
response = request.urlopen(req)

data = BeautifulSoup(response, 'html.parser')
# print(data.prettify())

print("\nEncabezado")
print(data.title.text)
p = data.find_all("div", {"data-section": "articleBody"})
print("\nCuerpo")
for i in p:
    print(i.text)
