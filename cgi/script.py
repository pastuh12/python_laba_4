#!D:\PycharmProjects\Individual_4\python.exe
import cgi, sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')
form = cgi.FieldStorage()
author_data = (form.getfirst("author-name"), form.getfirst("date-of-birth"),
               form.getfirst("place-of-birth"), form.getfirst("date-of-death"))
genre_data = (form.getfirst('genre'))
works_data = (form.getfirst("works-title"), form.getfirst("date-of-creation"))
author_id = 0
genre_id = 0
try:
    body = '<p>Обрабатывается форма</p>'
    con = sqlite3.connect('laba_4.db')
    cur = con.cursor()

    sql = 'INSERT INTO author(author_name, date_of_birth, place_of_birth, date_of_death) VALUES(?, ?, ?, ?);'
    cur.execute(sql, author_data)

    sql = 'SELECT author_id from author ORDER BY author_id DESC LIMIT 1;'
    cur.execute(sql)
    rows = cur.fetchone()
    for row in rows:
        author_id = int(row)

    sql = 'INSERT INTO works(works_title, date_of_creation, author_id, genre_id) VALUES(?, ?, ?, ?);'
    cur.execute(sql, (works_data[0], works_data[1], author_id, genre_data))
    con.commit()

    sql = 'SELECT genre_name from genre WHERE genre_id = %d;' % int(genre_data)
    cur.execute(sql)
    rows = cur.fetchone()
    for row in rows:
        genre_name = str(row)

    body += """
    <table>
        <tr>
            <td>Автор</td>
            <td>Дата рождения</td>
            <td>Место рождения</td>
            <td>Дата смерти</td>
            <td>Произведение</td>
            <td>Дата создания</td>
            <td>Жанр</td>
        </tr>
        <tr>
    """
    for data in author_data:
        body += "<td>" + data + "</td>"
    for data in works_data:
        body += "<td>" + data + "</td>"
    body += "<td>" + genre_name + "</td>"
    body += "</tr>"
    body += "</table>"
    body += '<p>Данные сохранены</p>'
except sqlite3.Error as error:
    body = "Ошибка при подключении к SQLite" + str(error)
finally:
    html = """
    <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
                 <style type="text/css">
                        td{
                            border: solid 1px;
                            padding: 10px 20px 0 0;
                        }
                </style>
            </head>
            <body>
                %s
            </body>
        </html>
        """ % body
    if (con):
        con.close()

    print(html)