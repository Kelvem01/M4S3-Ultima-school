# importando  requests e htmlsession 
from requests_html import HTMLSession

# criando uma seção HTTP  e usando o HTMLsession
sessao = HTMLSession()

# definindo url da pagina acessada 
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

# realizando uma requisição com a pagina 
resposta = sessao.get(url)

# criando uma lista vazia 
anuncios = []

# usando o metodo find do objeto HTML retornado na resposta para encontrar todos os links do anuncio 
links = resposta.html.find('#ad-list li a')

# iterando sobre os links encontrado da pagina 
for link in links:
    #extraindo o titulo de cada atributo"title" do elemento
    url_iphone = link.attrs['href']
    
    # fazendo a requisição GET ao url do anuncio 
    resposta_iphone = sessao.get(url_iphone)

    #extrair o titulo e o preco de cada anuncio 
    titulo = resposta_iphone.html.find('h1', first = True).text
    preco = resposta_iphone.html.find('h2', first = True).text
    
    #adicionando as informações do anuncio na lista de anuncios
    anuncios.append({
        'url': url_iphone,
        'titulo': titulo,
        'preco': preco

    })
    # imprimir o titulo na tela 
    print(anuncios)