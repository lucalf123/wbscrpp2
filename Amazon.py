import requests
from bs4 import BeautifulSoup
import pandas as pd

nome = input("Informe o produto: ")

response = requests.get(f'https://www.amazon.com.br/s?k={nome}')

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'a-section a-spacing-small s-padding-left-small s-padding-right-small'})

lista = []

for produto in produtos:

    titulo = produto.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})

    preco = produto.find('span', attrs={'class': 'a-price-whole'})

    centavos = produto.find('span', attrs={'class': 'a-price-fraction'})

    link = produto.find('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

    if preco is False:
        lista.append([titulo.text, 'S/A', link['href']])

    if preco and centavos:
        k = f"R$ {preco.text}{centavos.text}"
        lista.append([titulo.text, k, link['href']])


x = pd.DataFrame(lista, columns=['Título', 'Preço', 'Link'])
x.to_excel('Amazon.xlsx', index=False)