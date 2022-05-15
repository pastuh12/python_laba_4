import sqlite3
import sys
import xml.etree.ElementTree as ET
from create_html import create_page

sys.stdout.reconfigure(encoding='utf-8')

fileXml = 'import.xml'
title = "Экспортирование"
content = ''
try:
    con = sqlite3.connect('../bd/database.db')
    cur = con.cursor()
    tree = ET.parse(fileXml)
    root = tree.getroot()

    sql = 'INSERT INTO author(author_name, date_of_birth, place_of_birth, date_of_death) VALUES(?, ?, ?, ?);'
    values = []
    authors = root.findall('author')
    for author in authors:
        values.clear()
        for i in author:
            values.append(i.text)
        cur.execute(
            sql,
            values
        )

    sql = 'INSERT INTO store(title, address) VALUES(?, ?);'
    values = []
    stores = root.findall('store')
    for store in stores:
        values.clear()
        for i in store:
            values.append(i.text)
        cur.execute(
            sql,
            values
            )

    sql = 'INSERT INTO works(works_title, date_of_creation, author_id, genre, store_id) VALUES(?,?,?,?,?)'
    values = []
    works = root.findall('works')
    for work in works:
        values.clear()
        for i in work:
            values.append(i.text)
        cur.execute(
            sql,
            values
        )
    con.commit()
    content = "<h2>Данные успешно экспортированны</h2>"
except sqlite3.Error as error:
    content = "<h2>Ошибка при подключении к sqlite %s </h2>" % error
finally:
    if (con):
        con.close()
    create_page(title, content)