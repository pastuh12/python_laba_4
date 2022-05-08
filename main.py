import sqlite3
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

try:
    con = sqlite3.connect('laba_4.db')
    cur = con.cursor()
    print("Подключение к базе laba_4 прошло успешно")

    sql = '''
PRAGMA foreign_keys = OFF;
    DROP TABLE IF EXISTS author;
    DROP TABLE IF EXISTS genre;
    DROP TABLE IF EXISTS works;
    PRAGMA foreign_keys = ON;
    CREATE TABLE author(
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name VARCHAR(150),
    date_of_birth VARCHAR(25),
    place_of_birth VARCHAR(100),
    date_of_death VARCHAR(25)
    );
    CREATE TABLE genre(
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name VARCHAR(55)
    );
    CREATE TABLE works(
    works_id INTEGER PRIMARY KEY AUTOINCREMENT,
    works_title VARCHAR(100),
    date_of_creation VARCHAR(25),
    author_id INTEGER,
    genre_id INTEGER);

    INSERT INTO genre(genre_name) VALUES("Роман");
    INSERT INTO genre(genre_name) VALUES("Поэма");
    INSERT INTO genre(genre_name) VALUES("Баллада");
    '''

    cur.executescript(sql)
    con.commit()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (con):
        con.close()
        print("Соединение с SQLite закрыто")

server_address = ("localhost", 8000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']
http_server.serve_forever()
