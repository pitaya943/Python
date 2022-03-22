# coding:utf-8

import requests as rq
from bs4 import BeautifulSoup
import time


def sleeptime(hour, min, sec):
    return hour*3600 + min*60 + sec


# fp = open('spotifyRank.txt', 'w+')
tStart = time.time()

url = "https://kworb.net/spotify/artists.html"
url_response = rq.get(url)
soup = BeautifulSoup(url_response.text, "lxml")

count = 0  # count

for info in soup.find_all('tr', ['d0', 'd1'], limit=10):

    whole = info.find_all('td')
    rank = whole[0].text
    href = whole[1].find('a').get('href')
    artist = whole[1].text
    volume = whole[2].text

    print("Rank\tArtist\t\tTotal stream")
    content = rank + "\t" + artist + "\t" + volume + "\nLink: " + href + "\n"
    print(content)

    # fp.write(content)
    time.sleep(sleeptime(0, 0, 3))

tEnd = time.time()
costTime = tEnd - tStart
print('It cost %.2f sec' % costTime)

# fp.close()
