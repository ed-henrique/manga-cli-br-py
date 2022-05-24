from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from re import findall
from sys import argv
from time import sleep
from default_config import config
from download_imgs import download_imgs

URL_BASE = "https://mangalivre.net"

def click_next_page_button():
    next_page_button = driver.find_element(by=By.XPATH, value="//div[@class='page-next']")
    next_page_button.click()

def get_imgs_max(url):
    while True:
        driver.get(URL_BASE + url + "#/!page0")
        html = driver.find_element(by=By.XPATH, value="//html").get_attribute('outerHTML')
        soup = BeautifulSoup(html, features="lxml")
        imgs_max = int(findall('\d+', str(soup.find_all("div", class_="page-navigation")[0]))[1])
        err_test = soup.find_all("div", {"id": "cf-error-details"})
        if err_test == []:
            break
    return imgs_max

def get_manga_imgs(url, page, imgs_list):
    while True:
        driver.get(URL_BASE + url + "#/!page" + str(page))
        html = driver.find_element(by=By.XPATH, value="//html").get_attribute('outerHTML')
        soup = BeautifulSoup(html, features="lxml")
        err_test = soup.find_all("div", {"id": "cf-error-details"})
        if str(soup.find_all("img")) != []:
            if findall('"([^"]*)"', str(soup.find_all("img")[3])) != []:
                imgs_links = findall('"([^"]*)"', str(soup.find_all("img")[3]))[1]
        imgs_list.append(imgs_links)
        if err_test == []:
            break   
        print("Erro: deu BO em na página {}!".format(url))

try:
    driver = webdriver.Chrome(options=config())
    sleep(3)
    url = "/ler/-50kg-no-cinderella/online/335115/8-2"
    imgs_max = get_imgs_max(url)
    imgs = []
    for i in range(imgs_max):
        get_manga_imgs(url, i, imgs)
        click_next_page_button()
        sleep(1) # 0.6 foi o limite
    i = 0
    for img in imgs:
        download_imgs(img, "{:03d}.jpg".format(i))
        i += 1
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()