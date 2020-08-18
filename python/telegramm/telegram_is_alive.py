import telepot
import time

token = '1083778601:AAEm90CkozJzDT2RzCQwjzWdMJ98ztvd9iY'
bot = telepot.Bot(token)
stage = 0

def handle(msg):
    msg_id = msg['from']['id']
    msg_content = msg['text']
    bot.sendMessage(msg_id, f"현재 : {stage}단계 진행중 메세지 : {msg_content}")

bot.message_loop(handle)

while True:
    for i in range(0,5): # 1번 반복문
        time.sleep(1)
        stage = 1
    for i in range(0,5): # 2번 반복문
        time.sleep(1)
        stage = 2
    
