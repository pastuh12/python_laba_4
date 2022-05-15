import sys
import data_geter
from create_html import create_page

sys.stdout.reconfigure(encoding='utf-8')
title = 'Форма операции'
broker_options = ''
user_options = ''

users = data_geter.take_users_data()
for user in users:
    user_options += "<option value='%s'>%s</option>\n"% (user[0], user[1])
if(user_options == ''):
    user_options = "<option disabled >Пользователей в базе нет</option>\n"

brokers = data_geter.take_brokers_data()
for broker in brokers:
    broker_options += "<option value='%s'>%s</option>\n"% (broker[0], broker[1])
if(broker_options == ''):
    broker_options = "<option disabled >Брокеров в базе нет</option>\n"


content = f'''
  <form  action="/cgi-bin/script.py">
    <input type="hidden" value="operation" name="type"/>
    <div>
      <h4>Данные операции</h4>
      <input class="form-control" required placeholder="Дата открытия" name="date-of-open" /><br />
      <input class="form-control" required placeholder="Дата закрытия" name="date-of-close" /><br />
      <select class="mb-4" required required name="user-id" >
        {user_options}
      </select>      
      <input class="form-control" required placeholder="Сколько" name="value"/><br/>
      <select class="mb-4" name ="broker-id">
        {broker_options}
      </select>
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
  </form>
'''
create_page(title, content)