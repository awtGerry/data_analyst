from urllib import request
import re

def get_data(html):
    # quitamos la basura
    html = re.sub(r'\n|\t', '', html) # quitar saltos de linea y tabulaciones
    html = re.sub(r'\s+', ' ', html) # quitar espacios en blanco
    html = re.sub(r'<!--.*?-->', '', html) # quitar comentarios
    html = re.sub(r'<script.*?</script>', '', html) # quitar scripts
    html = re.sub(r'<style.*?</style>', '', html) # quitar estilos
    # dar formato a los datos
    html = re.sub(r'<div class="col-md-3 col-sm-12 blog-masonry-item (.*?)">', r'\n\1', html)
    # conseguir titulos
    titulo = re.findall(r'<h4><a href=".*?">(.*?)</a></h4>', html)
    # conseguir sede
    sede = re.findall(r'<span class="sub alt-font">(.*?)</span>', html)

    # objetos para nivel y sede
    doctorado = {}
    maestria = {}
    # filtrar
    for i in range(len(titulo)):
        if re.search(r'Doctorado', titulo[i]):
            if sede[i] in doctorado:
                doctorado[sede[i]].append(titulo[i])
            else:
                doctorado[sede[i]] = [titulo[i]]
        elif re.search(r'Maestría', titulo[i]):
            if sede[i] in maestria:
                maestria[sede[i]].append(titulo[i])
            else:
                maestria[sede[i]] = [titulo[i]]

    print('Doctorado')
    for key, value in doctorado.items():
        print(key, value)
    print('Maestría')
    for key, value in maestria.items():
        print(key, value)


url = 'https://centrosconahcyt.net/oferta-academica/'
html = request.urlopen(url).read()
html = html.decode('utf-8')
get_data(html)
