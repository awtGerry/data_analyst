# 2.- De las siguientes escuelas, con sus respectivas sedes, obtener los puntos anteriores: sedes, maestrías y doctorados.
# Nacionales:
# Universidad Nacional Autónoma de México (UNAM): puesto 93,Tecnológico de Monterrey (Tec):  puesto 184, Instituto Tecnológico Autónomo de México -ITAM: puesto 651,Universidad Panamericana (UP): puesto 661,Colegio de México (COLMEX): puesto 681,Universidad Iberoamericana (IBERO): puesto 691,Instituto Politécnico Nacional (IPN): puesto 741,Universidad Anáhuac: puesto 771,Universidad de Guadalajara (UdeG): puesto 851,Universidad Autónoma Metropolitana (UAM):puesto 901.
#
# Extranjeras:
# Instituto Tecnológico de Massachusetts (MIT)
# Universidad de Cambridge
# Universidad de Oxford
# Universidad Harvard
# Universidad Standford
# Colegio Imperial de Londres
# Universidad Nacional de Singapur
# ETH Zurich
# UCL
# Universidad de California, Berkeley (UBC)

from urllib import request
import re

def get_html(url):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = request.urlopen(req).read()
    html = html.decode('utf-8')
    html = re.sub(r'\n|\t', '', html) # quitar saltos de linea y tabulaciones
    html = re.sub(r'\s+', ' ', html) # quitar espacios en blanco
    html = re.sub(r'<!--.*?-->', '', html) # quitar comentarios
    html = re.sub(r'<script.*?</script>', '', html) # quitar scripts
    html = re.sub(r'<style.*?</style>', '', html) # quitar estilos
    # regresar string
    return html

def get_unam(html):
    # Buscar plan de estudios
    # <div class="gdlr-core-course-item-list "><a class="gdlr-core-course-item-link" href="https://www.posgrado.unam.mx/programa/derecho-doctorado/"><span class="gdlr-core-course-item-id gdlr-core-skin-caption">A3-P23-PE3</span><span class="gdlr-core-course-item-title gdlr-core-skin-title">Derecho</span><div class="gdlr-core-course-item-info-wrap"><div class="gdlr-core-course-item-info"><span class="gdlr-core-head">Nivel Académico : </span><span class="gdlr-core-tail">Doctorado</span></div><div class="gdlr-core-course-item-info"><span class="gdlr-core-head">Área de Conocimiento : </span><span class="gdlr-core-tail">III. Ciencias Sociales</span></div></div></a></div>
    # html = re.findall(r'<div class="gdlr-core-course-item-list ">(.*?)</div>', html)
    # fix findall not returning anything
    html = re.findall(r'<div class="gdlr-core-course-item-list .*?">(.*?)</div>', html)
    # html = re.findall(r'<a class="gdlr-core-course-item-link" href="(.*?)"><span class="gdlr-core-course-item-id gdlr-core-skin-caption">(.*?)</span><span class="gdlr-core-course-item-title gdlr-core-skin-title">(.*?)</span><div class="gdlr-core-course-item-info-wrap"><div class="gdlr-core-course-item-info"><span class="gdlr-core-head">Nivel Académico : </span><span class="gdlr-core-tail">(.*?)</span></div><div class="gdlr-core-course-item-info"><span class="gdlr-core-head">Área de Conocimiento : </span><span class="gdlr-core-tail">(.*?)</span></div></div></a>', html)

    # get plan de estudios (derecho, economia, enfermeria, etc)
    plan_estudios = []
    for i in html:
        plan_estudios.append(i[2])
    print(plan_estudios)

def get_data(html):
    html = re.sub(r'\n|\t', '', html) # quitar saltos de linea y tabulaciones
    html = re.sub(r'\s+', ' ', html) # quitar espacios en blanco
    html = re.sub(r'<!--.*?-->', '', html) # quitar comentarios
    html = re.sub(r'<script.*?</script>', '', html) # quitar scripts
    html = re.sub(r'<style.*?</style>', '', html) # quitar estilos
    # dar formato a la informacion
    html = re.sub(r'<div class="col-sm-6 itemposg blogBox">(.*?)</div>', r'\n\1', html)
    print(html)
    # conseguir todos los datos
    html = re.findall(r'<p><a href="(.*?)">(.*?)</a></p>', html)
    print(html)

# sedes
unam_sedes_url = "https://www.unam.mx/comunidad/estudiantes/facultades-y-escuelas"
unam_sedes = get_html(unam_sedes_url)
# buscar en ambas paginas
unam_oferta_url = "https://www.posgrado.unam.mx/oferta-academica/?nivel-academico=doctorado&area-de-conocimiento=&duracion=&course-keywords="
unam_oferta = get_html(unam_oferta_url)
unam_oferta_url = "https://www.posgrado.unam.mx/oferta-academica/page/2/?nivel-academico=doctorado&area-de-conocimiento&duracion&course-keywords"
unam_oferta2 = get_html(unam_oferta_url)
unam_oferta = unam_oferta + unam_oferta2
get_unam(unam_oferta)

url = "https://posgrados-panamericana.up.edu.mx/"
req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = request.urlopen(req).read()
html = html.decode('utf-8')
get_data(html)
# <div class="col-sm-6 itemposg blogBox"><div class="descPosg"><p><a href="http://posgrados-panamericana.up.edu.mx/cdmx/comunicacion/maestria-en-comunucaciones-de-marca">Maestría en Comunicaciones de Marca</a></p><small>CDMX</small></div></div>
