from bs4 import BeautifulSoup
from selenium import webdriver
import time
import math
import re

#Dado un html de superprof retorna una lista de tuplas
def get_teacher_list(html):
    list_ = []
    soup = BeautifulSoup(html, 'lxml')
    teachers = soup.find_all('li', class_='container see')
    for teacher in teachers:
        link = teacher.find('a')['href']
        nombre = teacher.find('div', {'data-announcement-name': True})['data-announcement-name']
        precio =  teacher.find('li', class_='pricing').find('span', class_='text').get_text().replace("$", "").replace(".", "").replace("/hr", "")
        precio = int(precio)
        rating = teacher.find('span', class_='emphasis')
        if rating is None:
            continue
        rating = float(rating.get_text())
        c_rating = teacher.find('span', string=re.compile(r'\(\d+ opiniones\)'))
        if c_rating is None:
            continue
        c_rating = int(re.search(r'\d+', c_rating.get_text()).group())
        list_.append((link, nombre, precio, rating, c_rating))
    list_ = sorted(list_, key=orden_ratings, reverse=True)
    return list_

#Ordenar las valoraciones ponderadas
def orden_ratings(teacher):
    return teacher[3] * math.log(1 + teacher[4])

#Dado un url lo pasa a get_teacher_list y retorna su lista
def get_list_from_link(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    html = driver.page_source
    driver.quit()
    return get_teacher_list(html)