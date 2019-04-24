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

    # try:
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         return response.text
    #     return None
    # except :
    #     return None

def parse_page(html):
    selector = etree.HTML(html)
    title = selector.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/a[2]/text()')
    links = selector.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/a[2]/@href')

    for i1,i2 in zip(title,links):
        big_list.append((i1,'http://www.java1234.com'+i2))
    return big_list





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='List_learning1',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into javaShare_book (title,links) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    big_list = []
    for item in range(218,297):
        url = 'http://www.java1234.com/a/javabook/javabase/list_65_'+str(item)+'.html'
        html = get_one_page(url)
        content = parse_page(html)
        insertDB(content)
        # time.sleep(1)




#
# create table javaShare_book(
# id int not null primary key auto_increment,
# title text,
# links text
# ) engine=InnoDB  charset=utf8;


# drop  table R_links;