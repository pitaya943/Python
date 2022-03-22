# coding:utf-8
import requests as rq
from bs4 import BeautifulSoup
import io
import time


def sleeptime(hour, min, sec):
    return hour*3600 + min*60 + sec


tStart = time.time()  # 計時開始
fp = io.open("Data.txt", "ab+")
i = 1
while i < 2:
    nextlink = "https://www.marry.com.tw/venue-shop-kwbt2004mmir0mmpg1mm"
    nl_response = rq.get(nextlink)  # 用 requests 的 get 方法把網頁抓下來
    soup = BeautifulSoup(nl_response.text, "lxml")  # 指定 lxml 作為解析器

    # 輸出排版後的 HTML 程式碼
    # print(soup.prettify())

    # 用soup.find() [只能找單一元素，可回傳成Text或Str屬性]
    # 用soup.find_all() [找所有元素，回傳符合內容成1個List]

    for url in soup.findAll('a', {'class': 'shop_name cltk_click'}):
        response = rq.get(url.get('href'))  # 用 requests 的 get 方法把網頁抓下來
        html_doc = response.text  # text 屬性就是 html 檔案
        soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器
        if soup.select('h1') != []:
            company = soup.select('h1')[0].find('a').text
            # 判斷是否有H1
            if company != '':
                # 服務內容(有打勾)
                pid = soup.findAll('li', {'class': 'icon-check'})
                Con = ",".join([p.text.strip() for p in pid])
                # 地址
                address = soup.findAll('ul', {'class': 'contacts_list'})[
                    0].find('span', {'class': 'contacts_info'}).text
                fp.write(company.encode('utf-8') + '='.encode('utf-8'))
                fp.write(Con.encode('utf-8') + '?'.encode('utf-8') +
                         address.encode('utf-8') + '\n'.encode('utf-8'))
                time.sleep(sleeptime(0, 0, 3))
    i = i + 1
tEnd = time.time()  # 計時結束
fp.close()
print("It cost %f sec" % (tEnd - tStart))  # 會自動做進位
