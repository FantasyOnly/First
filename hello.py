# 导入requests 模块
import requests
from bs4 import BeautifulSoup
import json
import xlrd
import xlwt
from xlutils.copy import copy
import os

# 直接写入
def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")

# 追加写入
def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")

# 读取xls
def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()

# 根据请求获取数据
def getData(web_url):
    # 给请求指定一个请求头来模拟chrome浏览器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    # web_url = 'http://api.map.baidu.com/place/v2/search?query=中学&region=昆明&output=json&ak=v4lCWa7LUMS571AaDfb4m3cQWi1mrPfS'
    # 像目标url地址发送get请求，返回一个response对象
    r = requests.get(web_url, headers=headers)
    # 获取网页中的class为cV68d的所有a标签
    print(r.encoding)
    # print(r.text)
    all_a = BeautifulSoup(r.text, 'lxml').find_all('p')
    finalList=[];
    for a in all_a:
        # 循环获取a标签中的style
        img_str = str(a.string)
        data=json.loads(img_str)
        for item in data['results']:
            list1=[];
            list1.append(item['name'])
            list1.append(item['location']['lng'])
            list1.append(item['location']['lat'])
            list1.append(item['address'])
            list1.append(item['province'])
            list1.append(item['city'])
            list1.append(item['area'])
            list1.append(item['uid'])
            finalList.append(list1)
        return finalList

if __name__ == "__main__":
    # 表格地址和名字
    book_name_xls = 'D:\ideaWork\PythonProject\poiData.xls'
    #表单名字
    sheet_name_xls = 'poi数据表'
    value_title = [["name","lng","lat","address","province","city","area","street_id","uid"],]
    if not os.path.exists(book_name_xls):
        write_excel_xls(book_name_xls, sheet_name_xls, value_title)
    web_url = 'http://api.map.baidu.com/place/v2/search?query=中学&region=昆明&output=json&ak=v4lCWa7LUMS571AaDfb4m3cQWi1mrPfS'
    finalList=getData(web_url)
    write_excel_xls_append(book_name_xls, finalList)
    read_excel_xls(book_name_xls)
