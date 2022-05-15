import cgi, sqlite3
import sys
from create_html import create_page

sys.stdout.reconfigure(encoding='utf-8')
form = cgi.FieldStorage()


def safe_user():
    user_data = (form.getfirst("name"),
                   form.getfirst("cash-account"))

    sql = 'INSERT INTO user(user_name, cash-account) VALUES(?, ?);'
    try:
        cur.execute(sql, user_data)
        con.commit()
    except Exception as error:
        print("\n\n\n\n" + error + "\n\n\n\n")

    title = "Данные пользователя сохранены"
    content = f'''
        <h2 class="mt-5">Данные об новом пользователе успешно сохранены</h2>
        <table class="table">
            <thead>
                <tr>
                    <td>Имя</td>
                    <td>У него денег</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{user_data[0]}</td>
                    <td>{user_data[1]}</td>
                </tr>
            </tbody>
    '''
    return create_page(title, content)

def safe_broker():
    broker_data = (form.getfirst("title"), form.getfirst("site"), form.getfirst("telephon"))

    sql = 'INSERT INTO broker(title, site, telephon) VALUES(?,?,?)'
    try:
        cur.execute(sql, broker_data)
        con.commit()
    except Exception as error:
        print("\n\n\n\n" + error + "\n\n\n\n")

    title = "Данные брокера сохранены"
    content = f'''
        <h2 class="mt-5">Данные о новом брокере успешно сохранены</h2>
        <table class="table">
            <thead>
                <tr>
                    <td>Название</td>
                    <td>Сайт</td>
                    <td>Телефон</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{broker_data[0]}</td>
                    <td>{broker_data[1]}</td>
                    <td>{broker_data[2]}</td>                    
                </tr>
            </tbody>
    '''
    return create_page(title, content)


def safe_operation():
    operation_data = (form.getfirst("user-id"),
                  form.getfirst("date-of-open"),form.getfirst("date-of-close"), form.getfirst("broker-id"),
                  form.getfirst("value"))

    sql = 'INSERT INTO operations(user_id, date_of_open, date_of_close, broker_id, value) VALUES(?,?,?,?,?)'
    try:
        cur.execute(sql, operation_data)
        con.commit()
    except Exception as error:
        print("\n\n\n\n" + error + "\n\n\n\n")

    title = "Данные произведения сохранены"
    content = f'''
        <h2 class="mt-5">Данные об новом авторе успешно сохранены</h2>
        <table class="table">
            <thead>
                <tr>
                    <td>ID пользователя</td>
                    <td>Дата открытия</td>
                    <td>Дата закрытия</td>
                    <td>ID брокера</td>
                    <td>Количество</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{operation_data[0]}</td>
                    <td>{operation_data[1]}</td>
                    <td>{operation_data[2]}</td>
                    <td>{operation_data[3]}</td>
                    <td>{operation_data[4]}</td>
                </tr>
            </tbody>
    '''
    return create_page(title, content)
    


form_type = form.getfirst("type")
con = sqlite3.connect('../bd/database.bd')
cur = con.cursor()

if (form_type == "user"):
    safe_user()
else:
    if (form_type == "broker"):
        safe_broker()
    else:
        if (form_type == "operation"):
            safe_operation()