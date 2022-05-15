import sys
from create_html import create_page

sys.stdout.reconfigure(encoding='utf-8')
title = 'Форма пользователя'
content = f'''
  <form  action="./script.py">
    <input type="hidden" value="user" name="type"/>
    <div>
      <h4>Данные пользователя</h4> 
      <input class="form-control" type="text" required placeholder="Имя пользователя" name="name" /><br />
      <input class="form-control" required placeholder="Сколько у него денег" name="cash-account" /><br />
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
  </form>
'''
create_page(title, content)