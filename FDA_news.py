# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:36:15 2023

@author: willy
"""

# 載入套件
from bs4 import BeautifulSoup # 網頁解析
import pandas as pd
import requests  # 發送 requests
import warnings
warnings.filterwarnings("ignore")


# 變數設置
headers = {"Content-Type": "text/html; charset=utf-8"}
url = 'https://www.fda.gov.tw/tc/sitelist.aspx?sid=103'
# 下一頁的url
# https://www.fda.gov.tw/tc/sitelist.aspx?sid=103&pn=2

# 發送 Requests
res = requests.post(url, headers=headers).content
# 解析網頁
soup = BeautifulSoup(res, 'html.parser')
# 找到資料，位於class = 'listTable'
table = soup.find('table', class_='listTable')
# 取出資料<td>中的資料
td_list = table.find_all('td')
# 取出個別欄位資料
# td_list_0 = td_list[::3]
td_list_1 = td_list[1::3]
td_list_2 = td_list[2::3]

link_list = []
title_list = []
# 取出<a>中的href, title
for td in td_list_1:
    if td.find('a') is not None:
        link = 'https://www.fda.gov.tw/tc/' + td.find('a').get('href')
        title = td.find('a').get('title')
        link_list.append(link)
        title_list.append(title)
# 取出發布日期
day_list = []
day = [td.text.split()[0] for td in td_list_2]
day_list = day_list + day


# 執行下一頁
# 變數設置
headers = {"Content-Type": "text/html; charset=utf-8"}
url = 'https://www.fda.gov.tw/tc/sitelist.aspx?sid=103&pn=2'
# 發送 Requests
res = requests.post(url, headers=headers).content
# 解析網頁
soup = BeautifulSoup(res, 'html.parser')
# 找到資料，位於class = 'listTable'
table = soup.find('table', class_='listTable')
# 取出資料<td>中的資料
td_list = table.find_all('td')
# 取出個別欄位資料
# td_list_0 = td_list[::3]
td_list_1 = td_list[1::3]
td_list_2 = td_list[2::3]

# 取出<a>中的href, title
for td in td_list_1:
    if td.find('a') is not None:
        link = 'https://www.fda.gov.tw/tc/' + td.find('a').get('href')
        title = td.find('a').get('title')
        link_list.append(link)
        title_list.append(title)
# 取出發布日期
day = [td.text.split()[0] for td in td_list_2]
day_list = day_list + day


# 合併程dataframe
df = pd.DataFrame([title_list, link_list, day_list], index = ['titel', 'link', 'day']).T

