# coding=utf-8
import os
import requests
from bs4 import BeautifulSoup

try:
    if not os.path.exists("./img"):
        os.mkdir("./img")
    for k in range(1, int(input("请输入爬取页数："))+1):
        print("正在爬取第{}页".format(k))
        if k == 1:
            url = "http://pic.netbian.com/4k/index.html"
        else:
            url = "http://pic.netbian.com/4k/index_{}.html".format(k)
        html = requests.get(url).text
        soup = BeautifulSoup(html, "lxml")
        imges = soup.find_all("img")
        for img in imges:
            src = img.get("src")
            new_src = "https://pic.netbian.com" + src
            print(new_src)
            img_data = requests.get(url).content
            img_name = src.split("/")[-1]
            with open(os.path.join("./img", img_name), "wb") as f:
                f.write(img_data)
                print(f"下载完成：{img_name}")
except Exception as e:
    print("下载图片时发生错误")
# img_html = requests.get(src).content
# img_name = src.split("/")[-1]  # 截取最后一节作为文件名
# with open("./img" + img_name, "wb") as f:
#     f.write(img_html)
#     print("正在下载：", img_name)
#     print("下载完成")
