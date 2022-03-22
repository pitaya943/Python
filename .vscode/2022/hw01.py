# coding:utf-8

from operator import delitem
import requests as rq
from bs4 import BeautifulSoup
from collections import OrderedDict
import csv

dataList = [['commentNumber', 'title', 'href', 'author', 'date']]

for index in range(4995, 5002):
    url = 'https://www.ptt.cc/bbs/Stock/index'+str(index)+'.html'
    print(url)

    url_response = rq.get(url)
    soup = BeautifulSoup(url_response.text, "lxml")

    for info in soup.find_all('div', 'r-ent'):

        temp_data = []
        temp_data.clear()

        if info.find('div', 'nrec') != None:
            commentNumber = info.find('div', 'nrec').text
            temp_data.append(commentNumber)
        else:
            temp_data.append('comment number is not found')

        if info.find('div', 'title').find('a') != None:
            titleText = info.find('div', 'title').find('a').text
            temp_data.append(titleText)
        else:
            temp_data.append('title is not found')

        if info.find('div', 'title').find('a') != None:
            hrefOfArticle = info.find(
                'div', 'title').find('a').get('href')
            temp_data.append(hrefOfArticle)
        else:
            temp_data.append('href is not found')

        if info.find('div', 'meta').find('div', 'author') != None:
            authorOfArticle = info.find(
                'div', 'meta').find('div', 'author').text
            temp_data.append(authorOfArticle)
        else:
            temp_data.append('author is not found')

        if info.find('div', 'meta').find('div', 'date') != None:
            dateOfArticle = info.find('div', 'meta').find('div', 'date').text
            temp_data.append(dateOfArticle)
        else:
            temp_data.append('date is not found')

        dataList.append(temp_data)

        print(temp_data)

print(dataList)

with open('ptt_stock.csv', 'w+', newline='', encoding='utf_8_sig') as file:
    writer = csv.writer(file)
    writer.writerows(dataList)
