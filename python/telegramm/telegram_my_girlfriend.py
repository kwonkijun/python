from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(token='1281403404:AAEW-knmZc14iyMsqNpNeMGTm0q-i8RH11o', use_context=True)
dispather = updater.dispatcher
updater.start_polling()

def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id
    
    if '사귈래?' in text:
        bot.send_message(chat_id=chat_id, text='님이 대화방을 나가셨습니다.')
    else : 
        bot.send_message(chat_id=chat_id, text='자꾸 연락하지마')

echo_handler = MessageHandler(Filters.text, handler)
dispather.add_handler(echo_handler)