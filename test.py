from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import json


driver = webdriver.Chrome()  
url = 'https://github.com/JefferMarcelino'

driver.get(url)

#driver.find_element(by=By.XPATH,value='//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[2]').click()

element = driver.find_element(by=By.XPATH,value='/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[2]/div/ol')
html_content = element.get_attribute("outerHTML")

soup = BeautifulSoup(html_content, "html.parser")
listOl = soup.find_all(name="li")

pinnedRepos = []

for li in listOl:
    li_span = li.find("span").text
    li_language = li.find("span", itemprop="programmingLanguage").text
    li_p = li.find("p").text

    obj = {
        "name": li_span,
        "language": li_language,
        "description": li_p.replace("\n", "").strip()
    }

    pinnedRepos.append(obj)

js = json.dumps(pinnedRepos)
fp = open("pinnedRepos.json", "w")
fp.write(js)
fp.close()

driver.quit()
