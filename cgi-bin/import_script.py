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

    con = sqlite3.connect('../bd/database.db')
    cur = con.cursor()
    column_name = [
        'author_name', 'date_of_birth', 'place_of_birth', 'date_of_death'
    ]
    sql = 'SELECT author_name, date_of_birth, place_of_birth, date_of_death FROM author WHERE author_name IS NOT NULL ;'
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        new_element = ET.Element('author')
        for i in range(len(row)):
            new_subelement = ET.SubElement(new_element, column_name[i])
            new_subelement.text = str(row[i])
        new_root.append(new_element)
    tree.write(fileXml, encoding='utf-8')

    column_name = ['title', 'address']
    sql = 'SELECT title, address FROM store  WHERE title IS NOT NULL;'
    cur.execute(sql)
    rows.clear()
    rows = cur.fetchall()
    for row in rows:
        new_element = ET.Element('store')
        for i in range(len(row)):
            new_subelement = ET.SubElement(new_element, column_name[i])
            new_subelement.text = str(row[i])
        new_root.append(new_element)

    column_name = ['works_title', 'date_of_creation', 'author_id', 'genre', 'store_id']
    sql = 'SELECT works_title, date_of_creation, author_id, genre, store_id FROM works WHERE works_title IS NOT NULL;'
    cur.execute(sql)
    rows.clear()
    rows = cur.fetchall()
    for row in rows:
        new_element = ET.Element('works')
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