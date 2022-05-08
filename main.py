import sqlite3
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

try:
    con = sqlite3.connect('./bd/laba_4.db')
    cur = con.cursor()
    print("Подключение к базе laba_4 прошло успешно")

    sql_file = open('./bd/sql_script.txt', 'r')
    sql = sql_file.read()

    cur.executescript(sql)
    con.commit()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
    print("Соединение с SQLite закрыто")
finally:
    if (con):
        con.close()

server_address = ("localhost", 8000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi']
http_server.serve_forever()
