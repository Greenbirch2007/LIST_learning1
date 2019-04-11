#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()

def get_one_page(url):

    driver.get(url)
    html = driver.page_source
    return html

def next_page():
    for i in range(1,36):  # selenium 循环翻页成功！
        driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div[1]/div[2]/a[last()-1]').click()
        time.sleep(1)
        html = driver.page_source
        return html

def parse_page(html):
    selector = etree.HTML(html)
    title = selector.xpath('//*[@id="content"]/div[5]/ul/li/div[1]/h3/a/text()')
    type = selector.xpath('//*[@id="content"]/div[5]/ul/li/div[1]/a/text()')
    links = selector.xpath('//*[@id="content"]/div[5]/ul/li/div[1]/h3/a/@href')
    stars = selector.xpath('//*[@id="content"]/div[5]/ul/li/div[1]/div/span[1]/em/text()')
    downloadNums = selector.xpath('//*[@id="content"]/div[5]/ul/li/div[1]/div/span[2]/text()')

    for i1,i2,i3,i4,i5 in zip(title,type,links,stars,downloadNums):
        big_list.append((i1,i2,"https://www.haolizi.net"+i3,i4,i5))
    return big_list





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='List_learning1',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into HLZ_CPlus (title,type,links,stars,downloadNums) values (%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    big_list = []
    url = 'https://www.haolizi.net/examples/cpp_1.html'

    html = get_one_page(url)
    content = parse_page(html)
    insertDB(content)
    while True:
        html = next_page()
        content = parse_page(html)
        insertDB(content)
        print(datetime.datetime.now())

#
# create table HLZ_CPlus(
# id int not null primary key auto_increment,
# title text,
# type text,
# links text,
# stars varchar(10),
# downloadNums varchar(10)
# ) engine=InnoDB  charset=utf8;


# drop  table R_links;