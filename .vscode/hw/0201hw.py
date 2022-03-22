# coding:utf-8
from bs4 import BeautifulSoup
import sqlite3

homework = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>回家作業</title>
</head>
<body>
<h1>國家首都資料表</h1>
<d1>
    <dt>華盛頓Washington</dt>
        <dd>美國首都</dd>
    <dt>東京Tokyo</dt>
        <dd>日本首都</dd>
    <dt>首爾Seoul</dt>
        <dd>韓國首都</dd>
</d1>
</body>
</html>
"""

soup = BeautifulSoup(homework, 'html.parser')
capital = soup.find_all('dt')
country = soup.find_all('dd')
dict = dict()
for index in range(len(capital)):
    dict[country[index].text] = capital[index].text
print('------- Hw01 -------\n')
print(dict, '\n')

print('------- Hw02 -------\n')
conn = sqlite3.connect('hw.db')
cursor = conn.cursor()
print("Successfully Connected to SQLite")

conn.execute("""CREATE TABLE homework(country,capital TEXT NOT NULL);""")
for index in range(3):
    sqlIn = """INSERT INTO homework(country, capital) VALUES('{0}', '{1}')""".format(
        country[index].text, capital[index].text)
    count = cursor.execute(sqlIn)
    print("++ Record inserted successfully into homework table: ", cursor.rowcount)

conn.commit()
cursor.execute('SELECT * FROM homework')
print('\n------ output ------\n')
for row in cursor.fetchall():
    print(row)
conn.close()
