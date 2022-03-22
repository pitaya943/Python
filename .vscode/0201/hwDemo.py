from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import matplotlib.pyplot as plt
import csv
import time

XPathOfCheckBox = [
    '//*[@id="ctl00_ctl00_ContentPlaceHolder1_SubContentPlaceHolder1_indi_pplv_1"]',
    '//*[@id="ctl00_ctl00_ContentPlaceHolder1_SubContentPlaceHolder1_indi_pplv_2"]',
    '//*[@id="cb_all"]',
    '//*[@id="cb_indi_group_0"]', '//*[@id="cb_indi_group_1"]', '//*[@id="cb_indi_group_2"]',
    '//*[@id="cb_indi_group_3"]', '//*[@id="cb_indi_group_4"]', '//*[@id="cb_indi_group_10"]',
    '//*[@id="cb_indi_group_11"]', '//*[@id="cb_indi_group_17"]', '//*[@id="cb_indi_group_18"]'
]

XPathOfItems = {
    'active': '//*[@id="ctl00_ctl00_ContentPlaceHolder1_SubContentPlaceHolder1_year_sec1"]/div[2]/div[1]/a[7]',
    'start': '//*[@id="ctl00_ctl00_ContentPlaceHolder1_SubContentPlaceHolder1_year_start"]',
    'end': '//*[@id="ctl00_ctl00_ContentPlaceHolder1_SubContentPlaceHolder1_year_end"]',
    'button': '//*[@id="ctl00_ctl00_ContentPlaceHolder1_SubContentPlaceHolder1_submit1"]'
}


def sleeptime(hour, min, sec):
    return hour*3600 + min*60 + sec


options = Options()
options.add_argument('--disable-notifications')

chrome = webdriver.Chrome('.vscode/chromedriver', chrome_options=options)
chrome.get('https://pop-proj.ndc.gov.tw/dataSearch.aspx?uid=59&pid=59')

for _ in XPathOfCheckBox:
    chrome.find_element_by_xpath(_).click()
    time.sleep(sleeptime(0, 0, 0.5))

active = chrome.find_element_by_xpath(XPathOfItems['active']).click()

startYear = Select(chrome.find_element_by_xpath(XPathOfItems['start']))
startYear.select_by_value('2000')
time.sleep(sleeptime(0, 0, 1))

endYear = Select(chrome.find_element_by_xpath(XPathOfItems['end']))
endYear.select_by_value('2040')
time.sleep(sleeptime(0, 0, 1))

searchButton = chrome.find_element_by_xpath(XPathOfItems['button']).click()

soup = BeautifulSoup(chrome.page_source, 'html.parser')
table = soup.find('table', 'tb')
infos = table.find_all('tr')

listOfAll = [[0]*42 for _ in range(10)]
index = 0
for content in infos:
    if index == 0:
        listOfAll[index][0] = content.find(id='b').text
        for i in range(len(content)):
            result = content.find(id='c' + str(i+1))
            if result != None:
                listOfAll[index][i+1] = int(result.text)
    else:
        listOfAll[index][0] = content.find(id='e' + str(index)).text
        for i in range(len(content)):
            indexID = 'c' + str(i) + ' e' + str(index)
            result = content.find(headers=indexID)
            if result != None:
                if 0 < index <= 3:
                    listOfAll[index][i] = int(result.text)
                else:
                    listOfAll[index][i] = float(result.text)
    index += 1
print(listOfAll)

with open('output.csv', 'w', newline='', encoding='utf_8_sig') as file:
    writer = csv.writer(file)
    writer.writerows(listOfAll)

chrome.quit()
