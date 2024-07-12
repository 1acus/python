# coding=utf-8
import os
import requests
import re
from bs4 import BeautifulSoup

if not os.path.exists("./123"):
    os.mkdir("./123")
url = 'https://wy.zone.ci/bugs.php'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("请求失败")
else:
    soup = BeautifulSoup(response.text, "lxml")
    pattern = r'^bug_detail\.php\?'
    match = re.search(pattern, url)
    adress = soup.find_all("a", attrs={"href": re.compile(pattern)})
    for url in adress:
        href = url.get("href")
        new_href = "https://wy.zone.ci/" + href
        name = new_href.split("wybug")
        response_ = requests.get(new_href, headers=headers)
        if response_.status_code == 200:
            html = response_.text
            with open("./123" + "/456.md", "a", encoding="utf-8") as f:
                f.write(html)
                print("成功")
        else:
            print("失败")
