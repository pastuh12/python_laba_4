


def create_page(title, content):
    page = f'''
        <!DOCTYPE html>
        <html lang="ru" xmlns="http://www.w3.org/1999/html">
          <head>
            <meta charset="UTF-8" />
            <title>{title}</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <link rel="stylesheet" href="style.css" />
            <script src="./cgi-bin/script.py"></script>
          </head>
          <body>
            <div class="container">
                <h1>{title}</h1>
                {content}
            </div>
          </body>
        </html>
    '''
    print(page)