from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Dado un html de superprof retorna una lista de tuplas (link, nombre, precio)
def get_teacher_list(html):
    list_ = []
    soup = BeautifulSoup(html, 'lxml')
    teachers = soup.find_all('li', class_='container see')
    for teacher in teachers:
        link = teacher.find('a')['href']
        nombre = teacher.find('div', {'data-announcement-name': True})['data-announcement-name']
        precio =  teacher.find('li', class_='pricing').find('span', class_='text').get_text().replace("$", "").replace(".", "").replace("/hr", "")
        precio = int(precio)
        list_.append((link, nombre, precio))
    return list_

#Dado un url lo pasa a get_teacher_list y retorna su lista
def get_list_from_link(url):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(10)
    html = driver.page_source
    driver.quit()
    return get_teacher_list(html)