import data_provider as prov
import logger as log

def name_view(name):
    data = prov.get_name(name)
    log.name_logger(data)
    return data

def phone_view (phone):
    data = prov.get_phone(phone)
    log.phone_logger(data)
    return data
