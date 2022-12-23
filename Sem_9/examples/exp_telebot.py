@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    return user_id



@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data.split('#')[0] == call.data.split('#')[1]:
        bot.send_message(call.message.TG_CHAT_ID,  '✅ Correct!')
    else:
        bot.send_message(call.message.TG_CHAT_ID,  '❌ Wrong!\n♻️ The answer is: %s' % call.data.split('#')[1])



@bot.message_handler(commands=['game', 'g'])
def game(message):
    list_of_words = load_my_dictionary(message.from_user.id)
    random.shuffle(list_of_words)
    while not len(list_of_words) < 4:
        current = list_of_words.pop()
        word = current[0]
        definition = current[1]
        all_answers = generate_answers(word, list_of_words)
        keyboard = generate_keyboard(all_answers, word)
        bot.send_message(message.from_user.id, definition, reply_markup = keyboard)
        time.sleep(7)
    bot.send_message(message.from_user.id, '📭 List is empty!')




game = telebot.CallbackGame() 

#add game_short_name value (despite the doc saying theres no  need to add it)
game.game_short_name="menu"

#Create the actual button
buttons = [[telebot.InlineKeyboardButton(text="Show Menu",callback_game=game)]] 

#Send game with custom inline button
keyboard_markup = telebot.InlineKeyboardMarkup(buttons)
context.bot.send_game(chat_id=update.effective_chat.id,game_short_name="menu",reply_markup=keyboard_markup)
  
import random

answers = ("да", "нет", "это возможно")
choice = random.choice(answers)
# print("Думаю, ", choice)
message = "Думаю, {}".format(choice)
bot.send_message(TG_CHAT_ID, message)

#принятие решения
def choose(): #def (define) - "определить" создание ф-ции
    answers = ("да", "нет", "это возможно")
    choice = random.choice(answers)
    message = "Думаю, {}".format(choice)
    bot.send_message(TG_CHAT_ID, message)
choose() #использование ф-циии
choose()

def choose(TG_CHAT_ID, question):
    answers = ("да", "нет", "это возможно")
    choice = random.choice(answers)
    message = "Думаю, {}".format(choice)
    bot.send_message(TG_CHAT_ID, message)
    print("Мне написал пользователь с ID:", TG_CHAT_ID)
    print("Он спрашивал:", question)
    print("Я ответил:", message)
# choose(TG_CHAT_ID, "Привет! Можно мне повысить зарплату?")

def reply(TG_CHAT_ID, text):
    print("Привет! Пользователь с ID {} написал мне: {}".format(TG_CHAT_ID, text))

bot = telebot.TeleBot(cnfg.TOKEN)


bot.CallbackContext(choose)  # <---- Новая строчка!
bot.run_bot()  # <---- Новая строчка!



@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.TG_CHAT_ID,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"https://habr.com/ru/users/lubaznatel/")


# первый ход
def choose(): #def (define) - "определить" создание ф-ции
    players = ['Пользователь', 'Bot']
    choice = random.choice(players)
    message = "Игру начнет {}".format(choice)
    bot.send_message(TG_CHAT_ID, message)
choose() #использование ф-циии

print('server start')
bot.infinity_polling()