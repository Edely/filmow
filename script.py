#!/usr/bin/env python
# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup

slug = input('Digite a slug do usuario:\n')
url_base = 'https://filmow.com/usuario/{}/filmes/ja-vi/?pagina={}'
r = requests.get(url_base.format(slug, 1))
page = BeautifulSoup(r.text, 'html5lib')
lista = page.select("#movies-list")[0]
numero_paginas = page.select('.pagination')[0].find('a', {'title': 'última página'})['href'].split('pagina=')[1]

for pagina in range(1, int(numero_paginas)+1):
    r = requests.get(url_base.format(slug, pagina))
    page = BeautifulSoup(r.text, 'html5lib')
    lista = page.select("#movies-list")[0]
    filmes = lista.find_all('li')
    print('================')
    print('=== PAGINA {} ==='.format(pagina))
    print('================')
    for filme in filmes:
        name = filme.find('span', {'class': 'title'}).text
        id_do_filme = filme['id']           
        movie_rating_average = filme.find('span', {'class': 'movie-rating-average'}).text
        user_rating_average = filme.find('div', {'class': 'user-rating'}).find('span', {'class', 'star-rating' })
        if user_rating_average is not None:
            user_rating_average = user_rating_average['title'].split(' ')[1]       
        else:       
            user_rating_average = 'None'

        with open('{}.csv'.format(slug), 'a') as csvfile:
            csvfile.write(name+';'+id_do_filme+';'+movie_rating_average+';'+user_rating_average)
            csvfile.write('\n')
            