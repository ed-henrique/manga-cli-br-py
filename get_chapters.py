from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from re import findall
from sys import argv
from default_config import config

URL_BASE = "https://unionleitor.top"

def get_manga_chapters(url, chapters_list):
    while True:
        driver.get(URL_BASE + url)
        html = driver.find_element(by=By.XPATH, value="//html").get_attribute('outerHTML')
        soup = BeautifulSoup(html, features="lxml")
        err_test = soup.find_all("div", {"id": "cf-error-details"})
        chapters_numbers = soup.find_all("span", class_="cap-text")
        chapters_links = soup.find_all("a", {"class": "link-dark"})
        if err_test == []:
            break   
        print("Erro: deu BO em na página {}!".format(url))

    i = 0
    for chapter in chapters_numbers:
        chapters_links[i] = findall('"([^"]*)"', str(chapters_links[i]))[2]
        chapters_list.append('"{}": "{}"'.format(str(chapter)[57:-7], str(chapters_links[i])))
        i += 1

try:
    driver = webdriver.Chrome(options=config())
    chapters = []
    get_manga_chapters(str(argv[1]), chapters)
    for chapter in chapters:
        with open('chapters_and_links.txt', 'a') as f:
            f.write(chapter + "\n")
    f.close()
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()