import sqlite3
import sys
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

fileXml = 'import.xml'
body = ''
try:
    con = sqlite3.connect('laba_4.db')
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
            values,
        )

    sql = 'INSERT INTO genre(genre_name) VALUES(?);'
    values = []
    genres = root.findall('genre')
    for genre in genres:
        for i in genre:
            values.clear()
            values.append(i.text)
        cur.execute(
            sql,
            values,
            )

    sql = 'INSERT INTO works(works_title, date_of_creation, author_id, genre_id) VALUES(?,?,?,?)'
    values = []
    works = root.findall('works')
    for work in works:
        values.clear()
        for i in work:
            values.append(i.text)
        cur.execute(
            sql,
            values,
        )
    con.commit()
except sqlite3.Error as error:
    body = "<p>Ошибка при подключении к sqlite%s </p>" % error
finally:
    body += 'Данные экспортированны'
    html = f'''
    <!DOCTYPE HTML>
                <html lang="ru">
                    <head>
                        <meta charset="utf-8">
                        <title>Эспорт данных</title>
                    </head>
                    <body>
                    {body}
                    </body>
                </html>
    '''

    if (con):
        con.close()
    print(html)