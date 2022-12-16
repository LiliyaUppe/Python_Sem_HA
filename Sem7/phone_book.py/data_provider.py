
def get_name():
    name = input('Input last name: ')
    return name

def get_phone():
    phone = input('Input phone number like +7 999 999 99 99: ')
    return phone


def data_collection():
    return (get_name(), get_phone())