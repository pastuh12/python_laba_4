import sqlite3
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

try:
    con = sqlite3.connect('./bd/database.db')
    cur = con.cursor()
    sql_file = open('./bd/sql_script.txt', 'r')
    sql = sql_file.read()

    cur.executescript(sql)
    con.commit()
    print("Подключение к базе database прошло успешно")
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
    print("Соединение с SQLite закрыто")
finally:
    if (con):
        con.close()

server_address = ("localhost", 8000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']
http_server.serve_forever()
