import urllib.request
import telebot
from telebot import types
bot1 = telebot.TeleBot ('---');
admlist1 = ('troy4510', 'babayaga', 'dedmoroz')

main1 = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
itembtn1 = types.KeyboardButton('Адрес сервера')
itembtn2 = types.KeyboardButton('Статистика за день')
itembtn3 = types.KeyboardButton('Кнопка')


main1.add(itembtn1, itembtn2, itembtn3)

print ('БОТ ЗАПУЩЕН...')

def msg(msg1):
    print (msg1)

def get_ext_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    #print(external_ip)
    return external_ip

@bot1.message_handler(commands=['start'])
def handle_start(message):
    bot1.reply_to(message,'Hello, ' + str(message.from_user.first_name),reply_markup=main1)


@bot1.message_handler(content_types=['text'])
def get1_text_messages(message):
    if message.text == "Адрес сервера":
        ip1 = get_ext_ip()
        ans1 = str('http://' + ip1 + ':5000')
        bot1.send_message(message.from_user.id, ans1)
        msg(f'запрос адреса от {message.from_user.first_name}')

    elif message.text == "Статистика за день":
        ip1 = get_ext_ip()
        ans1 = str('http://' + ip1 + ':5000/xomka')
        bot1.send_message(message.from_user.id, ans1)

    elif message.text == "Кнопка":
        bot1.send_message(message.from_user.id, "Динь-динь")

    else:
        bot1.send_message(message.from_user.id, "Моя твоя не понимать")
        msgstr1 = message.from_user.first_name + " say: " + message.text
        msg(str(msgstr1))

if __name__ == '__main__':
    bot1.polling(none_stop=True, interval=5)
