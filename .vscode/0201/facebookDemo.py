# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument('--disable-notifications')

chrome = webdriver.Chrome('.vscode/chromedriver', chrome_options=options)
chrome.get('https://www.facebook.com/')

email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

email.send_keys('jerru32112@yahoo.com.tw')
password.send_keys('pitaya512')  # password
password.submit()

time.sleep(3)
chrome.get('https://www.facebook.com/profile.php?id=100003121294484&sk=friends')

for _ in range(5):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

soup = BeautifulSoup(chrome.page_source, 'lxml')
infos = soup.find_all('div', 'buofh1pr hv4rvrfc')

with open('Friend.txt', 'w+') as file:
    for info in infos:
        name = info.find('span', 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db a5q79mjw g1cxx5fr lrazzd5p oo9gr5id')
        mutualFriend = info.find(
            'div', 'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql')
        if name != None:
            print(name.text, ':')
            file.write(name.text)
            file.write(':\t')

        if mutualFriend != None:
            print(mutualFriend.text)
            file.write(mutualFriend.text)
        file.write('\n')

chrome.quit()
