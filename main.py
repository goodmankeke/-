#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import random
from lxml import etree
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
from pymongo.results import InsertOneResult

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/57.0.2987.133 Safari/537.36",
    # chrome
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko)Version/5.0.1 Safari/537.36",
    # safafi
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",  # Firefox
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"  # IE
]
headers = random.choice(ua_list)
# print(headers)
url = "https://www.phb123.com/jiaoyu/gx/21950.html"


def get_html(url):
    """
    检查html资源是否有问题
    :param url:
    :return: html标签页
    """
    response = requests.get(url, headers={'User-Agent': headers})
    if str(response.status_code).startswith('2'):
        html = response.text.encode(response.encoding).decode('utf-8')
        return html
    else:
        print('error')


def crawl(html):
    """
    爬取文本
    :param html:
    :return: 一行行的文本标签
    """
    ulist = []
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        ele = tr.select('td')
        ss = list(ele[0].stripped_strings), list(ele[1].stripped_strings), list(ele[2].stripped_strings), list(
            ele[3].stripped_strings), list(ele[4].stripped_strings)
        ulist.append(ss)
    return ulist

    # ulist.append(ui)
    # return ulist


# def styles(ulist: list):
#     """
#     将内容提取成一个新的列表，每个字段单独一个列表
#     :param ulist:
#     :return: List
#     """
#     sslist = []
#     for i in range(len(ulist)):
#         ss = [str(ulist[i][1]).strip()], [str(ulist[i][3]).strip()], [str(ulist[i][5]).strip()], [
#             str(ulist[i][7]).strip()], [str(ulist[i][9]).strip()]
#         sslist.append(ss)
#     return sslist

def styles(ulist: list):
    """
    换成一个列表表示一行
    :param ulist:
    :return:
    """
    sse = []
    for i in ulist:
        u_list = []
        for j in i:
            ss = ''.join(j)
            u_list.append(ss)
        # print(u_list)
        sse.append(u_list)
    return sse[1:]
    # return stru_list


def save_content(styles):
    """
    转字典存入MOngoDB
    :param styles:
    :return:
    """
    client = MongoClient('mongodb://172.22.142.234:27017')  # 客户端连接
    db = client['school']  # 指定数据库
    schools = db.schol
    for i in styles:
        ss = {
            "名次": i[0],
            "学校名称": i[1],
            "星级排名": i[2],
            "办学层次": i[3],
            "总分": i[4]
        }
        x: InsertOneResult = schools.insert_one(ss)  # 一条条插入数据库
        print(x.inserted_id)


def save_mogodu():
    """
    连接测试MongoDB
    :return:
    """
    client = MongoClient('mongodb://172.22.142.234:27017')  # 客户端连接
    db = client['school']  # 指定数据库
    schools = db.schol  # 集合
    print(schools)
    user1 = {'id': '1', 'name': 'ben', 'age': 20}
    x: InsertOneResult = schools.insert_one(user1)
    print(type(x), x)
    print(x.inserted_id)


if __name__ == '__main__':
    html = get_html(url)
    content = crawl(html)
    styles = styles(content)
    save_content(styles)
    # save_mogodu()
