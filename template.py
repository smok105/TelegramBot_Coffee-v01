import config
import telebot

from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    sti = open('all for bot/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     "Добро пожаловать {0.first_name}\n Я помощник <b>{1.first_name}</b>\n Веди команды или выбери их "
                     ":\n /menu - для заказа \n /help - для помощи  ".format(message.from_user,
                                                                             bot.get_me()),
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Тут перечень команд которые помогут тебе разобраться в боте\n /start - начало "
                                      "бота! \n /menu - это кофейное меню \n /help - это команда с командами ")


@bot.message_handler(commands=['menu'])
def menu_message(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item1 = types.KeyboardButton("Напитки с собой")
    item2 = types.KeyboardButton("Кофе в зернах")
    item3 = types.KeyboardButton("Десерты")

    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбери из меню ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        if message.text == 'Напитки с собой':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

            item1 = types.KeyboardButton("Эспрессо")
            item2 = types.KeyboardButton("Фильтр", )
            item3 = types.KeyboardButton("Капучино Маленький")
            item4 = types.KeyboardButton("Капучино Большой")
            item5 = types.KeyboardButton("Флет вайт")
            item6 = types.KeyboardButton("Латте")
            item7 = types.KeyboardButton("Хенд Брю")
            item8 = types.KeyboardButton("Чай")
            item9 = types.KeyboardButton("Какао")
            item10 = types.KeyboardButton("Горячий Шоколад")

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

            sti = open('all for bot/coffee to go.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, "Выбери из меню ", reply_markup=markup)
        elif message.text == 'Кофе в зернах':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

            item1 = types.KeyboardButton("Кения Дорманс(Эспрессо)")
            item2 = types.KeyboardButton("Уганда(Эспрессо)")
            item3 = types.KeyboardButton("Колумбия Супремо(Альтернатива)")
            item4 = types.KeyboardButton("Эфиопия Ато-Тона(Альтернатива)")

            markup.add(item1, item2, item3, item4)

            sti = open('all for bot/top.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Отлично, выбери из кофе', reply_markup=markup)
        elif message.text == 'Десерты':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

            item1 = types.KeyboardButton("Печенье Арахисовое")
            item2 = types.KeyboardButton("Печенье Шоколадное")
            item3 = types.KeyboardButton("Печенье Кокосово-Клюквенное")
            item4 = types.KeyboardButton("Печенье Овсяное")
            item5 = types.KeyboardButton("Синабон")
            item6 = types.KeyboardButton("Пасха")

            markup.add(item1, item2, item3, item4, item5, item6)

            sti = open('all for bot/cokis.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Отлично, выбери десерт который желаешь приобрести', reply_markup=markup)
        # Тут пошел говно код в одну строчку
        elif message.text == 'Эспрессо':
            bot.send_message(message.chat.id,
                             'Заказ Эспрессо 45 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Фильтр':
            bot.send_message(message.chat.id,
                             'Заказ Фильтр-кофе 35 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Капучино Маленький':
            bot.send_message(message.chat.id,
                             'Заказ Капучино Маленький 35 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Капучино Большой':
            bot.send_message(message.chat.id,
                             'Заказ Капучино Большой 45 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Флет вайт':
            bot.send_message(message.chat.id,
                             'Заказ Флет вайт 45 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Латте':
            bot.send_message(message.chat.id,
                             'Заказ Латте 40 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Хенд Брю':
            bot.send_message(message.chat.id,
                             'Заказ Хенд Брю 45 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Чай':
            bot.send_message(message.chat.id,
                             'Заказ Чай 25 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Какао':
            bot.send_message(message.chat.id,
                             'Заказ Какао 35 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Горячий Шоколад':
            bot.send_message(message.chat.id,
                             'Заказ Горячий Шоколад 50 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        # Начинаються зерна в пачках
        elif message.text == 'Кения Дорманс(Эспрессо)':
            bot.send_message(message.chat.id,
                             'Заказ Кения Дорманс(Эспрессо) 220 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Уганда(Эспрессо)':
            bot.send_message(message.chat.id,
                             'Заказ Уганда(Эспрессо) ... грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Колумбия Супремо(Альтернатива)':
            bot.send_message(message.chat.id,
                             'Заказ Колумбия Супремо(Альтернатива) ... грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Эфиопия Ато-Тона(Альтернатива)':
            bot.send_message(message.chat.id,
                             'Заказ Эфиопия Ато-Тона(Альтернатива) ... грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        # Начала Десертов
        elif message.text == 'Печенье Арахисовое':
            bot.send_message(message.chat.id,
                             'Заказ Печенье Арахисовое ... грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Печенье Шоколадное':
            bot.send_message(message.chat.id,
                             'Заказ Печенье Шоколадное ... грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Печенье Кокосово-Клюквенное':
            bot.send_message(message.chat.id,
                             'Заказ Кокосово-Клюквенное ... грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Печенье Овсяное':
            bot.send_message(message.chat.id,
                             'Заказ Печенье Овсяное ... грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Синабон':
            bot.send_message(message.chat.id,
                             'Заказ Синабон 35 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        elif message.text == 'Пасха':
            bot.send_message(message.chat.id,
                             'Заказ Пасха 150 грн, если хочешь что нибудь еще нажми /menu')
            bot.send_message(message.chat.id, 'Бариста готовит заказ ❤')
            bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        else:
            sti = open('all for bot/error.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, "Я тебя не понимаю, выбери пожалуйста с меню")


# RUN
bot.polling(none_stop=True)
