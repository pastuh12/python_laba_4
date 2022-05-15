import sys
from create_html import create_page

sys.stdout.reconfigure(encoding='utf-8')
title = 'Форма брокера'
content = f'''
  <form  action="/cgi-bin/script.py">
    <input type="hidden" value="broker" name="type"/>
    <div class="">
      <h4>Данные магазина</h4>
      <input class="form-control" required placeholder="Название брокера" name="title" /><br />
      <input class="form-control" required placeholder="Сайт" name="site" /><br />
      <input class="form-control" required placeholder="Телефон" name="telephon" /><br />
    </div>
    <div>
      <button type="submit" class="btn btn-primary">Отправить</button>
    </div>
  </form>
'''
create_page(title, content)