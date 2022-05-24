from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from re import findall
import time
from default_config import config

MAX_PAGES = 329
URL_FOR_DB = "https://mangalivre.net/series/index/nome/todos?page="

def get_links_to_get_html():
    links = []
    for i in range(1, MAX_PAGES + 1):
        links.append(URL_FOR_DB + str(i))
    return links

def get_manga_info(url, titles_list):

    while True:
        driver.get(url)
        html = driver.find_element(by=By.XPATH, value="//html").get_attribute('outerHTML')
        soup = BeautifulSoup(html, features="lxml")
        err_test = soup.find_all("div", {"id": "cf-error-details"})
        series_titles = soup.find_all("span", class_="series-title")
        series_links = soup.find_all("a", {"class": "link-block"})
        if err_test == []:
            break   
        print("Erro: deu BO em na página {}!".format(url))

    i = 0
    for series in series_titles:
        series_links[i] = findall('"([^"]*)"', str(series_links[i]))[1]
        titles_list.append('"{}": "{}"'.format(str(series)[31:-12], str(series_links[i])))
        i += 1

try:
    driver = webdriver.Chrome(options=config())
    links = get_links_to_get_html()
    titles = []
    for link in links:
        get_manga_info(link, titles)
        time.sleep(5)
    for title in titles:
        with open('titles.txt', 'a') as f:
            f.write(title + "\n")
    f.close()
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()