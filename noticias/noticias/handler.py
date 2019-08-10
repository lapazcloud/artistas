from lxml import html
import requests

def handle(req):
    url = 'https://www.paginasiete.bo'
    pagina = requests.get(url + '/noticias/')
    codigo = html.fromstring(pagina.content)
    
    noticias = codigo.xpath('//h3[@class="titulo"]/a/text()')
    enlaces = codigo.xpath('//h3[@class="titulo"]/a/@href')
    
    respuesta = ""
    for id, noticia in enumerate(noticias):
        respuesta += "# " + noticia + "\n"
        respuesta += url + enlaces[id] + "\n\n"
    
    return respuesta
