import random
# 좋반
# 이요 이용 이여 부탁드려요 부탁요 부탁해요 감사요 감사해요 이욤 
# ~ ! :) ★ ♡ ♥ ^^ ☜ ㅎㅎ 
reply_list_insta = [
    ["좋반"],
    ["이요", "이용" ,"이여" ,"부탁드려요" ,"부탁요" ,"부탁해요" ,"감사요" ,"감사해요" ,"이욤"],
    ["~","!",":)","★" ,"♡" ,"♥", "^^" ,"☜" ,"ㅎㅎ"]
]

reply_list_blog = [
    ["좋은", "멋진", "깔끔한", "정말 좋은", "한눈에 쏙 들어오는", "정말 깔끔한", "정말 멋진"],
    ["포스팅", "블로그 글"],
    ["잘 보고갑니다 :)", "잘 보고 가요!!", "이네요 잘보고 갑니당 ㅎㅎ", "입니다! 감사해요", "이네요. 좋은 정보 감사합니다!! :)", "입니다^^ 잘보고 갈께요~", "고맙습니다~^^", "고마워요 :)", "고마워요 잘보고 갈께요~ㅎㅎㅎㅎ", "고맙습니다! 잘보고 갈께요~:)"],
    ["내일 비소식이 있던데 우산 꼭챙기고 나가세용!!", "비가 추적추적 내리니 센치해지는 밤이네요^^", "18일 비가 온다더라구요 오랜만에 비오는 것 같은데 운전조심하세요!", "전 새벽인데 잠이 안오네요, 블로그 작성방법을 좀더 연구하고 있어요!"]
]

def make_reply_insta():
    reply = reply_list_insta[0][0] + random.choice(reply_list_insta[1]) + random.choice(reply_list_insta[2])
    return reply

def make_reply_blog():
    reply = f'{random.choice(reply_list_blog[0])} {random.choice(reply_list_blog[1])} {random.choice(reply_list_blog[2])} {random.choice(reply_list_blog[3])}'
    return reply