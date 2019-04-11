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


def parse_page(html):
    selector = etree.HTML(html)
    title = selector.xpath('//*[@id="fontzoom"]/ul/li/a/text()')
    links = selector.xpath('//*[@id="fontzoom"]/ul/li/a/@href')
    desc_contents = selector.xpath('//*[@id="fontzoom"]/ul/li/div/p[1]/text()')

    for i1,i2,i3 in zip(title,links,desc_contents):
        big_list.append((i1,i2,i3))
    return big_list




def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='List_learning1',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into java1 (title,links,desc_contents) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    big_list = []
    for item in range(1,1736):
        url = 'https://www.2cto.com/kf/ware/java/news/'+ str(item) + '.html'
        html = get_one_page(url)
        time.sleep(1)
        content = parse_page(html)
        insertDB(content)



# create table java1(
# id int not null primary key auto_increment,
# title text,
# links text,
# desc_contents text
# ) engine=InnoDB  charset=utf8;


# drop  table java1;