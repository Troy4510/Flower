import urllib.request
import telebot
from telebot import types
import pygame
import pygame.camera

bot1 = telebot.TeleBot ('2108304241:AAFgaJLGr9pNFtdyW385ccIV0fG_c6c5PVY');
admlist1 = ('troy4510', 'babayaga', 'dedmoroz')

main1 = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
itembtn1 = types.KeyboardButton('Адрес сервера')
itembtn2 = types.KeyboardButton('Текущий статус')
itembtn3 = types.KeyboardButton('Получить фото')

main1.add(itembtn1, itembtn2, itembtn3)

print ('[start telebot]')

def msg(msg1):
    print (msg1)

def get_ext_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
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
        msg(f'[request server from] {message.from_user.first_name}')

    elif message.text == "Текущий статус":
        ans1 = str('в разработке')
        bot1.send_message(message.from_user.id, ans1)

    elif message.text == "Получить фото":
        #bot1.send_message(message.from_user.id, "обработка запроса...")
        try:
            pygame.camera.init()
            camlist = pygame.camera.list_cameras()
            bot1.send_message(message.from_user.id, f"камеры: {camlist}")
            if camlist:
                cam = pygame.camera.Camera(camlist[0], (640, 480))
                cam.start()
                for i in range(10):
                    image = cam.get_image()
                #ready = pygame.camera.Camera.query_image()
                #print(f'ready?: {ready}')
                pygame.image.save(image, "cam01.jpg")
                bot1.send_photo(message.chat.id, open('cam01.jpg', 'rb'))
                cam.stop()
        except:
            bot1.send_message(message.from_user.id, "камера не отвечает")

    else:
        bot1.send_message(message.from_user.id, "Неизвестная команда")
        msgstr1 = message.from_user.first_name + " say: " + message.text
        msg(str(msgstr1))

if __name__ == '__main__':
    msg('[bot is online]')
    bot1.polling(none_stop=True, interval=5)
