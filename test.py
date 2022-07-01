from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import json


options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options) 

data = [{}]

def getPinnedRepo():
    repoOl = driver.find_element(by=By.XPATH,value='/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[2]/div/ol')
    html_content = repoOl.get_attribute("outerHTML")
    soup = BeautifulSoup(html_content, "html.parser")
    listOl = soup.find_all(name="li")

    reposList = []

    for li in listOl:
        li_span = li.find("span").text
        
        try:
            li_language = li.find("span", itemprop="programmingLanguage").text
        except AttributeError:
            li_language = ""

        try:
            li_p = li.find("p").text
        except AttributeError:
            li_p = ""
        
        obj = {
            "name": li_span,
            "language": li_language,
            "description": li_p.replace("\n", "").strip()
        }

        reposList.append(obj)

    data[0]["repositories"] = reposList


def getUserInfo():
    userInfo = driver.find_element(by=By.XPATH, value='/html/body/div[4]/main/div[2]/div/div[1]/div')
    html_content = userInfo.get_attribute("outerHTML")
    soup = BeautifulSoup(html_content, "html.parser")

    name = soup.find("span", itemprop="name").text

    data[0]["userInfo"] = {
        "name": name.replace("\n", "").strip()    
    }


username = str(input("What is the GitHub username: "))
url = f'https://github.com/{username}'

print("Wait...")

driver.get(url)

getUserInfo()
getPinnedRepo()

js = json.dumps(data)
fp = open("data.json", "w")
fp.write(js)
fp.close()

driver.quit()

print("Done...")
