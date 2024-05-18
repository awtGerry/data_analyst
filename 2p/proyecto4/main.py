# De 10 páginas -ya sea de tiendas, cadenas comerciales o bodegas-,
# de cada departamento que lo conforman, obtener lo productos que ofrecen 
# y ponerlos en forma plana : # consecutivo, descripción del producto, marca
# y precio. Colocando el nombre de la tienda, cadena o bodega que corresponda
# en la parte superior.

import re
from urllib import request

hdr = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

def get_html(url):
    req = request.Request(url, headers=hdr)
    html = request.urlopen(req).read()
    html = html.decode('utf-8')
    html = re.sub(r'\n|\t', '', html) # quitar saltos de linea y tabulaciones
    html = re.sub(r'\s+', ' ', html) # quitar espacios en blanco
    html = re.sub(r'<!--.*?-->', '', html) # quitar comentarios
    html = re.sub(r'<script.*?</script>', '', html) # quitar scripts
    html = re.sub(r'<style.*?</style>', '', html) # quitar estilos
    # regresar string
    return html

# we send the html to get the data, what is the data of the title, description, mark and price to automate the process
def get_data(html, form, title, price, brand):
    # dar formato a los datos
    html = re.sub(form, r'\n\1', html)
    # print(html)
    # conseguir titulo
    titulo = re.findall(title, html)
    print(titulo)
    marca = ""
    if brand == "puntadelcielo" or brand == "Nike" or brand == "C&A" or brand == "Cuidado con el perro":
        marca = brand
    else:
        marca = re.findall(brand, html)
    print(brand)
    precio = re.findall(price, html)
    if len(precio) > 0 and isinstance(precio[0], tuple):
        precio = [''.join(i) for i in precio]
    print(precio)
    # product (title, brand, price)
    productos = list(zip(titulo, marca, precio))
    # categorizar productos
    for i in range(len(productos)):
        print(i+1, productos[i][0], productos[i][1], productos[i][2])

url1 = "https://www.marti.mx/hombre/ropa/jerseys"
url2 = "https://puntadelcielo.com.mx/collections/cafe-molido-y-de-grano"
url3 = "https://www.walmart.com.mx/browse/cervezas-vinos-y-licores/destacados-cervezas-vinos-y-licores/destacados-cervezas-vinos-y-licores/750004_1350050_1350051"
url4 = "https://www.nike.com/mx/w/hombres-calzado-nik1zy7ok"
url5 = "https://www.cyamoda.com/hombre/ropa/jeans/"
url6 = "https://www.cuidadoconelperro.com.mx/hombre/ropa/playeras"
url7 = "https://www.dportenis.mx/hombre-dportenis/calzado-hombre-dportenis/beisbol-hombre-dportenis"

# marti
print("Marti")
html1 = get_html(url1)
f1 = '<section class="vtex-store-components-3-x-container">(.*?)</section>'
t1 = r'<span class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body">(.*?)</span>'
p1 = r'<span class="vicomstudio-product-price-1-x-sellingPriceValue vicomstudio-product-price-1-x-sellingPriceValue--GlobalUI"><span class="vicomstudio-product-price-1-x-currencyContainer vicomstudio-product-price-1-x-currencyContainer--GlobalUI"><span class="vicomstudio-product-price-1-x-currencyCode vicomstudio-product-price-1-x-currencyCode--GlobalUI">.*?</span><span class="vicomstudio-product-price-1-x-currencyInteger vicomstudio-product-price-1-x-currencyInteger--GlobalUI">(.*?)</span><span class="vicomstudio-product-price-1-x-currencyGroup vicomstudio-product-price-1-x-currencyGroup--GlobalUI">,</span><span class="vicomstudio-product-price-1-x-currencyInteger vicomstudio-product-price-1-x-currencyInteger--GlobalUI">(.*?)</span><span class="vicomstudio-product-price-1-x-currencyDecimal vicomstudio-product-price-1-x-currencyDecimal--GlobalUI">.</span><span class="vicomstudio-product-price-1-x-currencyFraction vicomstudio-product-price-1-x-currencyFraction--GlobalUI">(.*?)</span></span></span>'
b1 = r'<span class="vtex-product-summary-2-x-productBrandName">(.*?)</span>'
get_data(html1, f1, t1, p1, b1)

# puntadelcielo
print("\nPunta del cielo")
html2 = get_html(url2)
f2 = '<div class="collection">(.*?)</div>'
t2 = r'<span class="text">(.*?)</span>'
p2 = r'<span class="price-item price-item--regular">(.*?)</span>'
b2 = 'puntadelcielo'
get_data(html2, f2, t2, p2, b2)

# walmart
print("\nWalmart")
html3 = get_html(url3)
f3 = r'<div class="flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl" data-testid="item-stack">(.*?)</div>'
t3 = r'<span data-automation-id="product-title" class="normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy">(.*?)</span>'
p3 = r'<div class="mr1 mr2-xl b black green lh-copy f5 f4-l" aria-hidden=".*?">(.*?)</div>'
b3 = r'<div class="mt2 mb1 b f6 black mr1 lh-copy">(.*?)</div>'
get_data(html3, f3, t3, p3, b3)

# nike
print("\nNike")
html4 = get_html(url4)
f4 = r'<div class="product-grid__items css-hvew4t" id="skip-to-products">(.*?)</div>'
t4 = r'<div class="product-card__title" id=".*?">(.*?)</div>'
p4 = r'<div class="product-price mx__styling is--current-price css-11s12ax" data-testid="product-price">(.*?)</div>'
b4 = "Nike"
get_data(html4, f4, t4, p4, b4)

# c&a
print("\nC&A")
html5 = get_html(url5)
# f5 = r'<div class="product"><div class="product-title">(.*?)</div></div>'
f5 = r'<div class="tile-body">(.*?)</div>'
t5 = r'<a class="link" href="(.*?)">(.*?)</a>'
p5 = r'<span class="value" content="(.*?)">(.*?)</span>'
b5 = "C&A"
get_data(html5, f5, t5, p5, b5)

# cuidado con el perro
print("\nCuidado con el perro")
html6 = get_html(url6)
f6 = r'<div class="b-grid____lDEW styles_c-product-grid__ihX4n" data-gutter="narrow" data-cols="2 xl-4" data-gap="16 xl-20">(.*?)</div>'
t6 = r'<span class="styles_name__mQp_f">(.*?)</span>'
# <span data-is-discount="false" class="styles_price___Ow_Q">$159.00</span>
p6 = r'<span data-is-discount="false" class="styles_price___Ow_Q">(.*?)</span>'
b6 = "Cuidado con el perro"
get_data(html6, f6, t6, p6, b6)

# dportenis
print("\nDportenis")
html7 = get_html(url7)
f7 = r'<div class="product_listing_container">(.*?)</div>'
t7 = r'<a aria-hidden="true" tabindex="-1" id=".*?" href=".*?">(.*?)</a>'
p7 = r'<span id="(.*?)" data-price="(.*?)" class="offer_Price sale_price hasOffer" style ="(.*?)">(.*?)</span>'
b7 = "Dportenis"
get_data(html7, f7, t7, p7, b7)
