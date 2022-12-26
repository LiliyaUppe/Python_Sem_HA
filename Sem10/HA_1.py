# Создать бота для вывода текущего курса валют(желательно запрос по конкретной валюте)
# /currency USD

import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('Your TOKEN')


@bot.message_handler(commands=['start'])
def hello_commands(message):
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id, "Добро пожаловать! Я, Бот по текущему курсу валют. Выбери команду '/currency USD' или '/help'")

@bot.message_handler(commands=['currency'])
def hello_commands(message):
    global chat_id
    chat_id = message.chat.id
    url = 'https://www.banki.ru/products/currency/cash/nizhniy_novgorod/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    mass = soup.find_all(class_='table-flex__cell table-flex__cell--without-padding padding-left-default')
    date_time_update = soup.find_all(class_='text-align-center font-size-small text-no-transform font-normal')
    print(mass)
    print(date_time_update)
    string = str(soup.find_all(class_='table-flex__cell table-flex__cell--without-padding padding-left-default')[0])
    print(string)
    currencyUSD = string[string.find('>')+1:string.find('</div>'):].replace(',', '.')
    print(currencyUSD)
    string2 = str(soup.find_all(class_='text-align-center font-size-small text-no-transform font-normal'))
    date_time = string2[string2.find('>')+1:string2.find('</div>'):]
    print(date_time)
    bot.send_message(chat_id, f'текущий курс доллара: {currencyUSD} RUB. {date_time}')


@bot.message_handler(commands=['help'])
def help_commands(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'данный бот предоставляет актуальную информацию  курса валют ЦБР. [currency USD] - курс доллара США')


print('server start')
bot.infinity_polling()