# -*- coding:utf8 -*-

# 写个小脚本就搞定了！
import re
import copy
import pymysql

import time
from selenium import webdriver
from lxml import etree
import datetime


#请求

def get_first_page():
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=bootstrap-tabler%E6%97%A5%E6%9C%9F%E6%90%9C%E7%B4%A2&oq=%25E6%2598%258E%25E6%2596%25B0%25E6%2597%25A5%25E8%25AF%25AD%25E5%25AD%25A6%25E6%25A0%25A1&rsv_pq=e254d91d004459a3&rsv_t=29188W4DkY5Ex%2BUYJxLpA%2FqCd9UlphY2nCE5gjDzTIYm9xOQIhmdVdMFZoU&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=5803&rsv_sug3=10&rsv_sug1=6&rsv_sug7=000&rsv_n=2&bs=%E6%98%8E%E6%96%B0%E6%97%A5%E8%AF%AD%E5%AD%A6%E6%A0%A1'
    driver.get(url)
    html = driver.page_source
    return html

# 把首页和翻页处理？

# def removeStall(i_list):
#     f_list = []
#
#     for item in i_list:
#         f_i = "".join(item.split(","))
#         f_list.append(f_i[:-1])
#     return f_list

def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！

    b_list = []
    selector = etree.HTML(html)

    l = []
    link = selector.xpath('//h3/a/@href')
    for ite in link:
        l.append((ite))








    return l





def next_page():

    for i in range(1, 88):  # selenium 循环翻页成功！
        try:

            driver.find_element_by_xpath('//*[@id="page"]/a[last()]').click()
            html = driver.page_source
            return html
        except:
            print("先略过～")

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='LL',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into bootstrap_table_datesearch_BD (f_link) values (%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass







if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)


    html = get_first_page()
    content = parse_html(html)
    insertDB(content)
    while True:
        time.sleep(3)
        html = next_page()
        content = parse_html(html)
        insertDB(content)
        print(datetime.datetime.now())





# 字段设置了唯一性 unique
# LINK
# create table bootstrap_table_datesearch_BD(
# id int not null primary key auto_increment,
# f_link text
# ) engine=InnoDB  charset=utf8;


# drop table bootstrap_table_datesearch_BD;
