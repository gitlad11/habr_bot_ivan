import time
from tkinter import E
from bs4 import BeautifulSoup
import requests

def parsing():
    
    url = 'https://habr.com/ru/all'
    response = requests.get(url)
    time.sleep(1)
    soup =  BeautifulSoup(response.text, 'lxml')  

    try:
        name = soup.find('a', "tm-article-snippet__title-link")
        query_string = 'https://habr.com' + name.attrs['href']
        first_post = requests.get(query_string)
        time.sleep(1)
        first_post_soup = BeautifulSoup(first_post.text, 'lxml')

    except Exception:
        return False
        
    finally:
        title = first_post_soup.find('h1', "tm-article-snippet__title tm-article-snippet__title_h1")
        body = first_post_soup.find('div', "tm-article-body")
        return { "title" : title.text, "body" : body.text }

 