from urllib import request
from bs4 import BeautifulSoup
import nltk
import json

hdr = {
    'User-Agent': 'Wget/1.13.4 (linux-gnu)',
    'Accept': '*/*'
}

noticia = "https://www.jornada.com.mx/2023/02/20/economia/021n1eco"

req = request.Request(noticia, headers=hdr)
response = request.urlopen(req).read().decode('utf-8')

data = BeautifulSoup(response, 'html.parser')
print(data.prettify())

print("\nEncabezado")
print(data.title.text)
p = data.find_all("div", {"id": "article-text"})
print("\nCuerpo")
for i in p:
    print(i.text)
