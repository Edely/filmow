#!/usr/bin/env python
# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup

slug = input('Digite a slug do usuario:\n')

url_base = 'https://filmow.com/usuario/{}/filmes/ja-vi/'.format(slug)

r = requests.get(url_base)

page = BeautifulSoup(r.text, 'html5lib')
lista = page.select("#movies-list")[0]

filmes = lista.find_all('li')
for filme in filmes:
    name = filme.find('span', {'class': 'title'}).text
    id_do_filme = filme['id']
    movie_rating_average = filme.find('span', {'class': 'movie-rating-average'}).text
    user_rating_average = filme.find('span', {'class': 'star-rating'}).text
    print(user_rating_average)
    for i in user_rating_average:
        print(i)
        # try:
        #     nota = int(i)
        # except:
        #     pass

    # print(name)
    # print(id_do_filme)
    # print(movie_rating_average)
    # print(nota)
    break


#print(filmes)

# <li class="span2 movie_list_item" data-item-pk="1173146029" data-movie-pk="200381" id="1173146029">
# <div class="user-rating">
# <span class="tip star-rating star-rating-small stars" title="Nota: 4 estrelas">
# <div class="stars empty">
# <img src="https://ui.fstatic.com/static/images/star_rating_empty.png"/>
# <img src="https://ui.fstatic.com/static/images/star_rating_empty.png"/>
# <img src="https://ui.fstatic.com/static/images/star_rating_empty.png"/>
# <img src="https://ui.fstatic.com/static/images/star_rating_empty.png"/>
# <img src="https://ui.fstatic.com/static/images/star_rating_empty.png"/>
# </div>
# <div class="average" style="width: 80.0%;">
# <div class="stars">
# <img src="https://ui.fstatic.com/static/images/star_rating_full.png"/>
# <img src="https://ui.fstatic.com/static/images/star_rating_full.png"/>
# <img src="https://ui.fstatic.com/static/images/star_rating_full.png"/>
# <img src="https://ui.fstatic.com/static/images/star_rating_full.png"/>
# <img src="https://ui.fstatic.com/static/images/star_rating_full.png"/>
# </div>
# </div>
# </span>
# </div>
# <span class="wrapper">
# <a class="cover tip-movie " data-movie-pk="200381" href="/a-mala-e-os-errantes-t200381/" title="A Mala e os Errantes">
# <img alt="A Mala e os Errantes (Tramps)" src="https://img.fstatic.com/E1iNKzpC1Z9BKHJOOZ5r1yZbmEc=/fit-in/134x193/smart/https://cdn.fstatic.com/media/movies/covers/2017/04/ac957a1dbe0cbcdb8ca2238e9d18b57828559e1b.jpg"/>
# <h3><span class="title">A Mala e os Errantes</span></h3>
# </a>
# <span class="movie-rating-average">3.0</span>
# <span class="badge badge-num-comments tip" title="26 comentários">26</span>
# <span class="legend"></span>
# </span>
# </li>
