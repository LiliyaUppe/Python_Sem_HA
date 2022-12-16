from user_interface import name_view
from user_interface import phone_view


def new_create(data, device = 1):
    name, phone = data
    style = 'style = "front-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += ' <p {}>Name: {} last_name</p>\n'\
            .format(style, name)
    html += ' <p {}>Phone: {} number</p>\n'\
            .format(style, phone) 
    html += '</body>\n <html>'

    with open('new_book.html', 'w') as page:
        page.write(html)
    return data 