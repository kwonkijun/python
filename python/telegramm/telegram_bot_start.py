import telepot

token = '1083778601:AAEm90CkozJzDT2RzCQwjzWdMJ98ztvd9iY'
mc = '1021336969'
bot = telepot.Bot(token)

def handle(msg):
    msg_id = msg['from']['id']
    msg_content = msg['text']
    if(msg_content == '살아있나?'):
        bot.sendMessage(msg_id, '살아있네~')

bot.message_loop(handle) # 메세지를 받으면 받을 때마다 어떤 행동을 하도록 만듦
while True: pass # 아무 일도 하지 않고 기다리도록 만든다. 