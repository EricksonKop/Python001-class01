import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://maoyan.com/films?showType=3'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
response = requests.get(url, user_agent=user_agent)
soup = bs(response.text, 'html.parser')
movies = soup.find_all('div', attrs={'class': 'movie-item-hover'})[:10]
movies_list = []
for movie in movies:
    title = movie.find_all('div', attrs={'class': 'movie-hover-title'})[0].find('span').text
    film_type = movie.find('div', attrs={'class': 'movie-hover-title'})[1].text
    film_time = movie.find('div', attrs={'class': 'movie-hover-title'})[3].text
    movies_list.append([title, film_type, film_time])
# df = pd.DataFrame(data=movies_list)
# df.to_csv("./test_work1.csv", encoding="utf-8-sig", mode="a+", header=False, index=False)
with open('test_work1.csv', 'a+') as f:
    for info in movies_list:
        f.write(','.join(info) + ',\n')
