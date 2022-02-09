import pandas as pd
import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'
produto_name = input('Qual produto? ')
produto_name.lower()
response = requests.get(url_base + produto_name)
site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'ui-search-result__wrapper'})

lista = []

for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})

    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    if centavos:
        k = f'R${real.text},{centavos.text}'
        lista.append([titulo.text, k, link['href']])

    else:
        k = f'R${real.text}'
        lista.append([titulo.text, k, link['href']])

grd = pd.DataFrame(lista, columns=['Titulo', 'Valor', 'link'])
grd.to_excel('MercadoLivre.xlsx', index=False)
