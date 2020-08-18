import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
		[InlineKeyboardButton(text='네이버 블로그 검색', callback_data='naver_blog')],
		[InlineKeyboardButton(text='네이버 이미지 검색', callback_data='naver_img')]
	])
	
	bot.sendMessage(chat_id, '채팅봇이 제공하고 있는 기능입니다.', reply_markup=keyboard)

def on_callback_query(msg):
	query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
	print('Callback Query:', query_id, from_id, query_data)
	
	if(query_data == 'naver_blog'):
		bot.sendMessage(from_id, '네이버 블로그 검색을 선택하셨습니다.')
	elif(query_data == 'naver_img'):
		bot.sendMessage(from_id, '네이버 이미지 검색을 선택하셨습니다.')

	bot.answerCallbackQuery(query_id, text='Got it')

bot = telepot.Bot('1083778601:AAEm90CkozJzDT2RzCQwjzWdMJ98ztvd9iY')
MessageLoop(bot, {'chat': on_chat_message, 'callback_query':on_callback_query}).run_as_thread()

print('Listening....')

while True:
	pass
