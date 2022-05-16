import sqlite3
import sys
import xml.etree.ElementTree as ET
from create_html import create_page
sys.stdout.reconfigure(encoding='utf-8')

con = None
content = ''
title = "Импортирование"
try:
    fileXml = 'import.xml'
    file = open(fileXml, 'w', encoding='utf-8')
    file.write('<?xml version="1.0" encoding="UTF-8"?>\n\t')
    file.write('<root>\n\t')
    file.write('</root>\n\t')
    file.close()
    tree = ET.parse(fileXml)
    new_root = tree.getroot()

    con = sqlite3.connect('./bd/database.db')
    cur = con.cursor()
    column_name = [
        'name', 'cash_account']
    sql = 'SELECT name, cash_account FROM users WHERE name IS NOT NULL ;'
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        new_element = ET.Element('user')
        for i in range(len(row)):
            new_subelement = ET.SubElement(new_element, column_name[i])
            new_subelement.text = str(row[i])
        new_root.append(new_element)
    tree.write(fileXml, encoding='utf-8')

    column_name = ['title', 'site', 'telephon']
    sql = 'SELECT title, site, telephon FROM brokers  WHERE title IS NOT NULL;'
    cur.execute(sql)
    rows.clear()
    rows = cur.fetchall()
    for row in rows:
        new_element = ET.Element('broker')
        for i in range(len(row)):
            new_subelement = ET.SubElement(new_element, column_name[i])
            new_subelement.text = str(row[i])
        new_root.append(new_element)

    column_name = ['user_id', 'date_of_open', 'date_of_close', 'broker_id', 'value']
    sql = 'SELECT user_id, date_of_open, date_of_close, broker_id, value FROM operations WHERE user_id IS NOT NULL;'
    cur.execute(sql)
    rows.clear()
    rows = cur.fetchall()
    for row in rows:
        new_element = ET.Element('operation')
        for i in range(len(row)):
            new_subelement = ET.SubElement(new_element, column_name[i])
            new_subelement.text = str(row[i])
        new_root.append(new_element)

    tree.write(fileXml, encoding='utf-8')
    con.commit()

    content += "<h2>Данные импортированы</h2>"
except sqlite3.Error as error:
    content = "<h4>Ошибка при подключении к sqlite %s</h4>" % error
finally:
    if (con):
        con.close()
    create_page(title, content)