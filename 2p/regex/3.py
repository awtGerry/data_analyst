from urllib import request
from bs4 import BeautifulSoup
import nltk
import json

hdr = {
    'User-Agent': 'Wget/1.13.4 (linux-gnu)',
    'Accept': '*/*'
}

noticia = "https://www.jornada.com.mx/noticia/2024/04/16/politica/amlo-nada-que-negociar-con-ecuador-se-dirimira-todo-en-la-cij-733"

req = request.Request(noticia, headers=hdr)
response = request.urlopen(req).read().decode('utf-8')

# Get id where the article starts
# where Qué difícil se ha vuelto tener una conversación que no esté en los extremos.

data = BeautifulSoup(response, 'html.parser')
print(data.prettify())

print("\nEncabezado")
print(data.title.text)
p = data.find_all("div", {"id": "content_nitf"})
print("\nCuerpo")
for i in p:
    print(i.text)
