from urllib import request
import re

def get_data(html):
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
    # conseguir areas
    areas = re.findall(r'<span class="sub alt-font" style="text-transform: none; font-weight: 100">(.*?)</span>', html)

    # objetos para nivel, sede y area
    doctorado = {}
    maestria = {}
    # filtrar
    for i in range(len(titulo)):
        # encuentra doctorado
        if re.search(r'Doctorado', titulo[i]):
            # si la sede ya existe en el diccionario
            if sede[i] in doctorado:
                doctorado[sede[i]].append((titulo[i], areas[i]))
            else:
                doctorado[sede[i]] = [(titulo[i], areas[i])]

            # agregar area
        elif re.search(r'Maestría', titulo[i]):
            if sede[i] in maestria:
                maestria[sede[i]].append(titulo[i])
            else:
                maestria[sede[i]] = [titulo[i]]

    # Imprimir todos los datos
    print('Doctorado')
    for key, value in doctorado.items():
        print(key, value)
    print('Maestría')
    for key, value in maestria.items():
        print(key, value)

    # Imprimir solo los datos de la sede seleccionada ejemplo
    sede_seleccionada = 'COLSAN'
    print('Doctorado en', sede_seleccionada)
    for key, value in doctorado.items():
        if key == sede_seleccionada:
            # dar formato titulo: area
            for i in value:
                print(i[0], ':', i[1])

    # Imprimir todo de Coordinación de Física, matemáticas y ciencias de datos
    area_seleccionada = 'Coordinación de Física, matemáticas y ciencias de datos'
    print(area_seleccionada)
    for key, value in doctorado.items():
        for i in value:
            if i[1] == area_seleccionada:
                print("Sede:", key, "->", i[0])


url = 'https://centrosconahcyt.net/oferta-academica/'
html = request.urlopen(url).read()
html = html.decode('utf-8')
get_data(html)
