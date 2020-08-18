from urllib import request
from urllib import parse
from bs4 import BeautifulSoup

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

import os, errno

my_token = '1083778601:AAEm90CkozJzDT2RzCQwjzWdMJ98ztvd9iY'

savePath = "D:\\temp\\"
# 폴더 만들기 f
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")

path = 'D:/temp/lion.png'

def callback_func(bot, update):
    update.message.reply_text("사자사진을 검색합니다.")
    base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
    plus_url = parse.quote_plus('사자')
    url = base_url + plus_url
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html-parser')
    img = soup.select_one('div.img_area > a.thumb._thumb > img')
    update.message.reply_text(img.string)
    request.urlretrieve(img['data-source'], path)
    bot.send_photo(chat_id=update.message.chat_id, photo=open("D:/temp/lion.png", 'rb'))

updater = Updater(my_token)
command_handler = CommandHandler('lion', callback_func)
updater.dispatcher.add_handler(command_handler)
updater.start_polling(clean=True)
updater.idle()
