#%% FDA的公告檢驗方法

# 載入套件
from bs4 import BeautifulSoup # 網頁解析
import pandas as pd
import requests  # 發送 requests
from datetime import datetime


# 變數設置
headers = {"Content-Type": "text/html; charset=utf-8"}
url = 'https://www.fda.gov.tw/tc/sitelist.aspx?sid=103'
# https://www.fda.gov.tw/tc/sitelist.aspx?sid=103&pn=2    # 下一頁的url

list_url = [f'{url}', f'{url}&pn=2']

# 建立存放資料的list
list_link = []
list_title = []
list_day = []

for u in list_url:
    # 發送 Requests
    res = requests.post(u, headers=headers).content
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
            list_link.append(link)
            list_title.append(title)
    # 取出發布日期
    day = [td.text.split()[0] for td in td_list_2]
    list_day = list_day + day

# 合併程dataframe
df = pd.DataFrame([list_title, list_link, list_day], index = ['titel', 'link', 'day']).T

# 取得現在時間
current_date = datetime.now().date()
current_date = str(current_date).replace("-", "")

# 儲存資料
df.to_csv(fr'C:\Users\user\Downloads\{current_date}_FDA公告檢驗方法.csv', index = False, encoding = 'utf-8-sig')

#%% FDA本署新聞

# 載入套件
from bs4 import BeautifulSoup # 網頁解析
import pandas as pd
import requests  # 發送 requests
from datetime import datetime


# 變數設置
headers = {"Content-Type": "text/html; charset=utf-8"}
url = 'https://www.fda.gov.tw/TC/news.aspx?cid=4'
# https://www.fda.gov.tw/tc/sitelist.aspx?sid=103&pn=2    # 下一頁的url

list_url = [f'{url}', f'{url}&pn=2']

# 建立存放資料的list
list_link = []
list_title = []
list_day = []

for u in list_url:
    # 發送 Requests
    res = requests.post(u, headers=headers).content
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
            list_link.append(link)
            list_title.append(title)
    # 取出發布日期
    day = [td.text.split()[0] for td in td_list_2]
    list_day = list_day + day

# 合併程dataframe
df = pd.DataFrame([list_title, list_link, list_day], index = ['titel', 'link', 'day']).T

# 取得現在時間
current_date = datetime.now().date()
current_date = str(current_date).replace("-", "")

# 儲存資料
df.to_csv(fr'C:\Users\user\Downloads\{current_date}_FDA本署新聞.csv', index = False, encoding = 'utf-8-sig')
