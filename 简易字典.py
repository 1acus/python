# coding=utf-8
def link(url):
    if "://" in url:
        url = url.split("https://")[1]
    if "/" in url:
        url = url.replace("/", "")
    main = url.split(".")
    black = ['www', 'com', 'cn', 'net', 'org', 'gov', 'cc', 'biz', 'info', 'mobi', 'name', 'pro', 'xxx', 'xyz', 'top', 'vip',]
    white = []
    for key in main:
        if key not in black:
            white.append(key)
            return white


if __name__ == '__main__':
    print(link(input("输入网址：")))
