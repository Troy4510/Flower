import telebot
from telebot import types
bot1 = telebot.TeleBot ('2108304241:AAFgaJLGr9pNFtdyW385ccIV0fG_c6c5PVY');
admlist1 = ('troy4510', 'babayaga', 'dedmoroz')

main1 = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
itembtn1 = types.KeyboardButton('Привет')
itembtn2 = types.KeyboardButton('ComScan')
itembtn3 = types.KeyboardButton('Data_tst')
itembtn4 = types.KeyboardButton('HIGH')
itembtn5 = types.KeyboardButton('LOW')
itembtn6 = types.KeyboardButton('LLS_connect')
itembtn7 = types.KeyboardButton('LLS_read')
main1.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5, itembtn6, itembtn7)
comlist1 = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)

print ('БОТ ЗАПУЩЕН...')

def msg(msg1):
    print (msg1)

@bot1.message_handler(commands=['start'])
def handle_start(message):
    bot1.reply_to(message,'Hello, ' + str(message.from_user.first_name),reply_markup=main1)


@bot1.message_handler(content_types=['text'])
def get1_text_messages(message):
    if message.text == "Привет":
        bot1.send_message(message.from_user.id, message.from_user.first_name + ", Здаровати дебилоид!")
        msg(f'бот приветствует {message.from_user.first_name}')

    elif message.text == "HIGH":
        if message.from_user.first_name == admlist1[0]:
            bot1.send_message(message.from_user.id, "SET HIGH")
            msg(f'{message.from_user.first_name} SET HIGH')
        else:
            bot1.send_message(message.from_user.id, "ты не админ чтоб кнопкой щёлкать")
            msg(f'{message.from_user.first_name} не администратор для этой комманды!')
        # ser1.write(b'1')

    elif message.text == "LOW":
        bot1.send_message(message.from_user.id, "SET LOW")
        msg(f'{message.from_user.first_name} SET LOW')
        # ser1.write(b'0')

    elif message.text == 'Data_tst':
        bot1.send_message(message.from_user.id, "высылаю твои данные на сервер")
        msg('\n')
        msg(f'FAT ID FROM: {message.from_user.first_name}')
        msg('\n')
        # print(type(message))
        msg(message)
        # for x in range(0,50,1): print(message[x])

    else:
        bot1.send_message(message.from_user.id, "Моя твоя не понимать")
        msgstr1 = message.from_user.first_name + " say: " + message.text
        msg(str(msgstr1))


bot1.polling(none_stop=True, interval=5)