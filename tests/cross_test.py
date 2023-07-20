from flask import Flask             #основа
from flask import request           #запросы
from flask import render_template   #шаблоны
app = Flask(__name__)

import telebot
from telebot import types
bot1 = telebot.TeleBot ('2108304241:AAFgaJLGr9pNFtdyW385ccIV0fG_c6c5PVY');
admlist1 = ('troy4510', 'troy')

import threading
import time
from datetime import datetime

