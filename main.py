import telebot
from telebot import types
bot = telebot.TeleBot('5861860868:AAHR0Exo_FtaKHyjg3cH01pW8Yfbghl7tOY')
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуйте,<b>{message.from_user.first_name}</b>, Вас приветствует строительная компания ДомСтрой!🤩'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    choice = types.KeyboardButton('Оформление заказа.')
    job_list = types.KeyboardButton('Свободные вакансии.')
    our_info = types.KeyboardButton('Подробнее.')
    report = types.KeyboardButton('Отзыв')
    markup.add(choice, job_list, our_info, report)
    bot.send_message(message.chat.id, 'Главное меню:', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        if message.text == 'Отзыв':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            back = types.KeyboardButton('Вернуться назад👈')
            report = types.KeyboardButton('Отлично⭐⭐⭐⭐⭐')
            report2 = types.KeyboardButton('Хорошо⭐⭐⭐⭐')
            report3 = types.KeyboardButton('Пойдёт⭐⭐⭐')
            report4 = types.KeyboardButton('Плохо⭐⭐')
            report5 = types.KeyboardButton('Ужасно⭐')
            report6 = types.KeyboardButton('Очень ужасно🤮')
            markup.add(back,report, report2, report3, report4, report5, report6)
            bot.send_message(message.chat.id, 'Отзыв:', reply_markup=markup)
        elif message.text == 'Очень ужасно🤮':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            back = types.KeyboardButton('Вернуться назад👈')
            markup.add(back)
            bot.send_message(message.chat.id, 'Твой отзыв не кому не нужен.')
        elif message.text == 'Отлично⭐⭐⭐⭐⭐':
            bot.send_message(message.chat.id, 'Спасибо за отзыв!')
        elif message.text == 'Хорошо⭐⭐⭐⭐':
            bot.send_message(message.chat.id, 'Спасибо за отзыв!')
        elif message.text == 'Пойдёт⭐⭐⭐':
            bot.send_message(message.chat.id, 'Спасибо за отзыв!')
        elif message.text == 'Плохо⭐⭐':
            bot.send_message(message.chat.id, 'Спасибо за отзыв!')
        elif message.text == 'Ужасно⭐':
            bot.send_message(message.chat.id, 'Спасибо за отзыв! Впредь мы будем внимательны!')
        elif message.text == 'Подробнее.':
            keyboard = types.InlineKeyboardMarkup()
            url_btn = types.InlineKeyboardButton(text="Подробнее переходите на наш сайт:", url='https://emmmabk.github.io/DomStroy/')
            # url
            keyboard.add(url_btn)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            back = types.KeyboardButton('Вернуться назад👈')
            markup.add(back)
            bot.send_message(message.chat.id, 'Смотреть ниже👇', reply_markup=keyboard)
            bot.send_message(message.chat.id, '---------------', reply_markup=markup)
            # Через Github сделать сайт ии его домен за деплойить на сервер и скинуть сюда ссылку
        elif message.text == 'Свободные вакансии.':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            back = types.KeyboardButton('Вернуться назад👈')
            markup.add(back)
            bot.send_message(message.chat.id,'На данный момент у нас нет свободных вакансий🥲', reply_markup=markup)
        elif message.text == 'Оформление заказа.':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            home = types.KeyboardButton('Дом.')
            bath = types.KeyboardButton('Баня.')
            besedka = types.KeyboardButton('Беседка.')
            hoz_build = types.KeyboardButton('Хоз. постройки.')
            back = types.KeyboardButton('Вернуться назад👈')
            markup.add(home, bath, besedka, hoz_build, back)
            bot.send_message(message.chat.id, 'Оформление заказа.', reply_markup=markup)
        elif message.text == 'Вернуться назад👈':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            choice = types.KeyboardButton('Оформление заказа.')
            job_list = types.KeyboardButton('Свободные вакансии.')
            our_info = types.KeyboardButton('Подробнее.')
            report = types.KeyboardButton('Отзыв')
            markup.add(choice, job_list, our_info, report)
            bot.send_message(message.chat.id, 'Главное меню:', reply_markup=markup)
        elif message.text == 'Дом.':
            bot.send_message(message.chat.id, 'Введите размер: _ кв. м.')
            bot.send_message(message.chat.id, 'Введите кол-во этажей: _ этаж(ей/a).')
            bot.send_message(message.chat.id, 'Есть ли фундамент?')
            bot.send_message(message.chat.id, 'Перейдите на страницу оформления заказа.')
            keyboard = types.InlineKeyboardMarkup()
            translate = types.InlineKeyboardButton(text='Нажмите сюда✊', url='https://www.youtube.com/')
            keyboard.add(translate)
            bot.send_message(message.chat.id, 'Ссылка на оформление заказа снизу👇', reply_markup=keyboard)
        elif message.text == 'Баня.':
            bot.send_message(message.chat.id, 'Введите размер: _ кв. м.')
            bot.send_message(message.chat.id, 'Введите кол-во этажей: _ этаж(ей/a).')
            bot.send_message(message.chat.id, 'Есть ли фундамент?')
            bot.send_message(message.chat.id, 'Введите все данные в формате X / X / Да/Нет.')
            keyboard = types.InlineKeyboardMarkup()
            translate = types.InlineKeyboardButton(text='Нажмите сюда✊', url='https://www.youtube.com/')
            keyboard.add(translate)
            bot.send_message(message.chat.id, 'Ссылка на оформление заказа снизу👇', reply_markup=keyboard)
        elif message.text == 'Беседка.':
            bot.send_message(message.chat.id, 'Введите размер: _ кв. м.')
            bot.send_message(message.chat.id, 'Введите кол-во этажей: _ этаж(ей/a).')
            bot.send_message(message.chat.id, 'Есть ли фундамент?')
            bot.send_message(message.chat.id, 'Введите все данные в формате X / X / Да/Нет.')
            keyboard = types.InlineKeyboardMarkup()
            translate = types.InlineKeyboardButton(text='Нажмите сюда✊', url='https://www.youtube.com/')
            keyboard.add(translate)
            bot.send_message(message.chat.id, 'Ссылка на оформление заказа снизу👇', reply_markup=keyboard)                 
        elif message.text == 'Хоз. постройки.':
            bot.send_message(message.chat.id, 'Введите размер: _ кв. м.')
            bot.send_message(message.chat.id, 'Введите кол-во этажей: _ этаж(ей/a).')
            bot.send_message(message.chat.id, 'Есть ли фундамент?')
            bot.send_message(message.chat.id, 'Введите все данные в формате X / X / Да/Нет.')
            keyboard = types.InlineKeyboardMarkup()
            # url
            keyboard.add(translate)
            bot.send_message(message.chat.id, 'Ссылка на оформление заказа снизу👇', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, 'Я вас не понимаю, используйте кнопки!')
bot.polling(none_stop=True)