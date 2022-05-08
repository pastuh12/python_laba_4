from cgitb import html
import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')
try:
    con = sqlite3.connect('./db/laba_4.db')
    cur = con.cursor()
    cur.execute('''
        SELECT a.author_name, a.date_of_birth, a.place_of_birth, a.date_of_death, w.works_title,
        w.date_of_creation, g.genre_name FROM author a JOIN works w ON (a.author_id = w.author_id)
        JOIN genre g ON (w.genre_id = g.genre_id);
        ''')
    rows = cur.fetchall()
    cur.execute('SELECT author_name FROM author')
    f = cur.fetchall()
    body = f'<b> {len(f)}</b>'
    if rows.__len__() == 0:
        body = '<p>База данных пуста</p>'
    else:
        body = '''
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
        '''
        for row in rows:
            body += '<tr>'
            for i in range(len(row)):
                body += '<td>'
                body += row[i]
                body += '</td>'
            body += '</tr>'
    body += '</table>'
except sqlite3.Error as error:
    body = '<p>Ошибка при подключении к sqlite', '</p>'
finally:
    if (con):
        con.close()
    htm = '''
    <!DOCTYPE HTML>
            <html lang="ru">
                <head>
                    <meta charset='utf-8'>
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
    ''' % body
    print(htm)