from bs4 import BeautifulSoup
import requests

with open("test.html", "r") as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    teachers = soup.find_all('li', class_='container see')
    for teacher in teachers:
        print(teacher)