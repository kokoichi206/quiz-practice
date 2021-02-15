import requests
import urllib.request
import os
from bs4 import BeautifulSoup
import re


# 全メンバーの顔写真を取得
def scraping_allpic():

    ## アクセスするurl
    TOP_URL = "https://www.nogizaka46.com/member"



    # BeautifulSoupオブジェクト生成
    headers = {"User-Agent": "Mozilla/5.0"}

    soup = BeautifulSoup(requests.get(TOP_URL, headers=headers).content, 'html.parser')
    details = soup.findAll("div", class_="unit")


    names = {}
    for detail in details:
        nameJa = detail.find("a").find(class_="main").text

        href = detail.find("a").get("href")
        memberURL = href[1:]
        name = href[9:-4]

        names[name] = nameJa

    return names


if __name__ == '__main__':
    names = scraping_allpic()
    with open('names.txt', mode='w') as f:
        for nameEn, nameJa in names.items():
            # f.write('{' + nameEn + ': ' + '"' + nameJa + '"},\n')
            f.write('["' + nameEn + '", ' + '"' + nameJa + '"],\n')
