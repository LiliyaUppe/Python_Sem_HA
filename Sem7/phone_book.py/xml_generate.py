from user_interface import name_view
from user_interface import phone_view

def new_create(data, device = 1):
    name, phone = data
    xml = '<xml>\n'
    xml += ' < name = "Last name"> {}</name>\n'\
        .format(name)
    xml += ' < phone = "number"> {}</phone>\n'\
        .format(phone) 
    xml += '<xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)
    return data