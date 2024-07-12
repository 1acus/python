# coding=utf-8
import requests
from optparse import OptionParser
import sys


def get_url(url, filename):
    # 导入字典，url和目录拼接，发起请求，通过响应码判断是否存在目录
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    with open('%s.txt' % filename, 'r') as f:
        for i in f:
            res = url + i.strip()
            r = requests.get(res, headers=headers, timeout=1)
            try:
                if r.status_code == 200:
                    print('[*]'+res)
                else:
                    pass
            except Exception as e:
                print(e)


def main():
    # 设置命令行参数
    parser = OptionParser()
    parser.add_option('-u', '--url', type='string', dest='url', help='目标url')
    parser.add_option('-f', '--filename', type='string', dest='filename', help='字典文件名')
    (options, args) = parser.parse_args()
    if options.url and options.filename:
        get_url(options.url, options.filename)
    else:
        parser.print_help()
        sys.exit()


if __name__ == '__main__':
    url = input('请输入目标url: ')
    filename = input('请输入字典文件名: ')
    start = get_url(url, filename)
    print(start.get('url'))
