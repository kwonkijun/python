import telepot
from urllib import request 
from urllib import parse
from bs4 import BeautifulSoup
import time

token = '1083778601:AAEm90CkozJzDT2RzCQwjzWdMJ98ztvd9iY'
bot = telepot.Bot(token)
search = False

def handle(msg) : 
    global search
    msgId = msg['from']['id']
    msgContents = msg['text']
    if (msgContents == '네이버 블로그 검색') :
        bot.sendMessage(msgId, '좋아요 어떤 검색어를 입력하고 싶나요 ?')
        search=True
    elif (search is True):
        blogCrawling(msgId, msgContents)
        search=False
    else:
        bot.sendMessage(msgId, '잘 모르겠어요')

def blogCrawling(msgId, msgContents) :
    search = parse.quote_plus(msgContents)

    url = F'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={search}&sm=tab_pge&srchby=all&st=sim&where=post&start=1'

    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    itemList = soup.select_one('#elThumbnailResultArea')
    items = itemList.select('li')

    bot.sendMessage(msgId, '상위 5개의 검색어를 뽑아왔어요')

    for idx, lists in enumerate(items, 1) :
        title = lists.select_one('dl > dt > a').get_text()
        date = lists.select_one('dl > dd.txt_inline').get_text()
        post = lists.select_one('dl > dd.sh_blog_passage').get_text()
        bot.sendMessage(msgId, F'{idx}. {title} {date} {post}')
        if(idx == 5):
            break
     
bot.message_loop(handle)
while True : pass