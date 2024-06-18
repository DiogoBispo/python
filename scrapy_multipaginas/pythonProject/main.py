import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.amazon.com.br/s?k=Sansung&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1F6NDLGFNSREW&sprefix=sansung%2Caps%2C270&ref=nb_sb_noss_2'
headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"}

def proxima_pagina(soup):
    #procura botao proxima
    paginas = soup.find('a', {'s-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})
    #ir para ultima pagina com o botao proximo desativado
    if not paginas.find  ('span', {'class': 's-pagination-item s-pagination-next s-pagination-disabled'}):
        url = 'https://www.amazon.com.br/'
        prox = soup.find('a', 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator', href= True )
        url_final = (url + str(prox['href']))
        return url_final
    else:
        return
while True:

    site = requests.get(url, headers= headers)
    soup = BeautifulSoup(site.content,'html.parser')
    url = proxima_pagina(soup)
    time.sleep(400)
    if not url:
        break
    print(url)
