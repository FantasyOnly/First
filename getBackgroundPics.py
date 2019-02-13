# 导入requests 模块
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 给请求指定一个请求头来模拟chrome浏览器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    web_url = 'https://unsplash.com'
    # 像目标url地址发送get请求，返回一个response对象
    r = requests.get(web_url, headers=headers)
    # 获取网页中的class为cV68d的所有a标签
    print(r.encoding)
    # print(r.text)
    all_a = BeautifulSoup(r.text, 'lxml').find_all('img',class_='_2zEKz')
    for a in all_a:

        # 循环获取a标签中的style
        img_str = a['srcset']
        print (type(img_str))

        print('标签是：',img_str)

        first_pos = img_str.index('2400w,')+6
        second_pos = img_str.index('2592w')
        print(img_str[first_pos: second_pos])
        break