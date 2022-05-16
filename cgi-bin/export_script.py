import sqlite3
import sys
import xml.etree.ElementTree as ET
from create_html import create_page

sys.stdout.reconfigure(encoding='utf-8')

fileXml = 'import.xml'
title = "Экспортирование"
content = ''
try:
    con = sqlite3.connect('./bd/database.db')
    cur = con.cursor()
    tree = ET.parse(fileXml)
    root = tree.getroot()

    sql = 'INSERT INTO users(name, cash_account) VALUES(?,?);'
    values = []
    users = root.findall('user')
    for user in users:
        values.clear()
        for i in user:
            values.append(i.text)
        cur.execute(
            sql,
            values
        )

    sql = 'INSERT INTO brokers(title, site, telephon) VALUES(?, ?, ?);'
    values = []
    brokers = root.findall('broker')
    for broker in brokers:
        values.clear()
        for i in broker:
            values.append(i.text)
        cur.execute(
            sql,
            values
            )

    sql = 'INSERT INTO operations(user_id, date_of_open, date_of_close, broker_id, value) VALUES(?,?,?,?,?)'
    values = []
    operation = root.findall('operation')
    for work in operation:
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