import sqlite3
import sys
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

con = None
body = ''
try:
    fileXml = 'import.xml'
    file = open(fileXml, 'w', encoding='utf-8')
    file.write('<?xml version="1.0" encoding="UTF-8"?>\n\t')
    file.write('<root>\n\t')
    file.write('</root>\n\t')
    file.close()
    tree = ET.parse(fileXml)
    new_root = tree.getroot()

    con = sqlite3.connect('laba_4.db')
    cur = con.cursor()
    column_name = [
        'author_name', 'date_of_birth', 'place_of_birth', 'date_of_death'
    ]
    body = '<p>Началось экспортирование данных</p>'
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
    sql = 'SELECT genre_name FROM genre  WHERE genre_name IS NOT NULL;'
    cur.execute(sql)
    rows.clear()
    rows = cur.fetchall()
    for row in rows:
        new_element = ET.Element('genre')
        for i in row:
            new_subelement = ET.SubElement(new_element, 'name' )
            new_subelement.text = i
        new_root.append(new_element)

    column_name = ['works_title', 'date_of_creation', 'author_id', 'genre_id']
    sql = 'SELECT works_title, date_of_creation, author_id, genre_id FROM works WHERE works_title IS NOT NULL;'
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

    body += '<p>Данные импортированы</p>'
except sqlite3.Error as error:
    body = "<p>Ошибка при подключении к sqlite %s</p>" % error
finally:
    if (con):
        con.close()
    html = """
    <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="utf-8">
                <title>Импортирование</title>
            </head>
            <body>
                %s
            </body>
        </html>
    """ % body
    print(html)