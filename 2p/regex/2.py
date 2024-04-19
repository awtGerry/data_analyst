from urllib import request
from bs4 import BeautifulSoup
import nltk
import json

hdr = {
    'User-Agent': 'Wget/1.13.4 (linux-gnu)',
    'Accept': '*/*'
}

noticia = "https://www.eluniversal.com.mx/elecciones/claudia-sheinbaum-propone-sistema-de-inteligencia-e-investigacion-para-atender-delitos-de-mayor-impacto/"

req = request.Request(noticia, headers=hdr)
response = request.urlopen(req).read().decode('utf-8')

data = BeautifulSoup(response, 'html.parser')

print("\nEncabezado")
print(data.title.text)
p = data.find_all("div", {"role": "main"})
print("\nCuerpo")
for i in p:
    print(i.text)
