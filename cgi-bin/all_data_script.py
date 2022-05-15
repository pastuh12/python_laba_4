from cgitb import html
from http.client import HTTPResponse
import sqlite3
import sys
from create_html import create_page



sys.stdout.reconfigure(encoding='utf-8')
content = '''
    <table class="table mt-5">
        <thead>
            <tr>
                <td>Операция</td>
                <td>Дата открытия</td>
                <td>Дата закрытия</td>
                <td>Количество</td>
                <td>Брокер</td>
                <td>Сайт</td>
                <td>Телефон</td>
                <td>Пользователь</td>
                <td>Денежный счет</td>
            </tr>
        </thead>
        <tbody>
'''
title = "Все данные"
try:
    con = sqlite3.connect('../bd/database.db')
    cur = con.cursor()
    cur.execute(
        'SELECT o.id, o.date_of_open, o.date_of_close, o.value, b.title, b.site, b.telephon, u.name, u.cash_account FROM operations o JOIN brokers b ON (o.broker_id = b.id) JOIN users u ON (o.user_id = u.id) WHERE b.tittle IS NOT NULL;'
    )
    rows = cur.fetchall()
    print(rows, file=sys.stdout)
    if len(rows) == 0:
        content = '<h2>База данных пуста</h2>'
    else:
        for row in rows:
            content += '<tr>'
            for i in range(len(row)):
                content += f'''
                    <td> 
                        {str(row[i])}
                    </td>'''
            content += '</tr>'
        content += '</tbody>'
        content += '</table>'
except sqlite3.Error as error:
    content = '<h2>Ошибка при подключении к sqlite' + str(error) + '</h2>'
finally:
    if (con):
        con.close()
    create_page(title, content)        


