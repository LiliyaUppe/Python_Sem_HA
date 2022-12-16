import csv
def name_phone_logger(data):
    with open('book.csv', 'a', encoding='utf-8') as file:
        headline = ["Name", "Phone_number"]
        # file_writer = csv.DictWriter(file, fieldnames=headline)
        file_writer = csv.DictWriter(file, delimiter = ',', lineterminator="\r", fieldnames=headline)
        file_writer.writeheader()
        file_writer = csv.writer(file, delimiter = ',')
        file_writer.writerow(data)


# def name_logger(data):
#     with open('book.csv', 'a') as file:
#         # file.write('name|| phone\n {}\n'.format(data))
#         file.write(f'name || phone\n {data}\n')


# def phone_logger(data):
#     with open('book.csv', 'a') as file:
#         # file.write('phone||{}\n'.format(data))
#         file.write(f'phone || {data}\n')
  

import csv
def name_phone_logger(data):
    with open('book.csv', 'w', encoding='utf-8') as file:
        headline = ["Name", "Phone_number"]
        # file_writer = csv.DictWriter(file, fieldnames=headline)
        file_writer = csv.DictWriter(file, delimiter = '|', lineterminator="\r", fieldnames=headline)
        file_writer.writeheader()
        file_writer = csv.writer(file, delimiter = '|')
        file_writer.writerow(data)