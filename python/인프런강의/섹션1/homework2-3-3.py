# 과제_1
# 네이버 홈페이지 배너 광고 추출해서 C드라이브에 저장하기 
# 비디오 파일도 저장해 볼 것! 

import urllib.request as req

imgURL = "https://ssl.pstatic.net/tveta/libs/1279/1279525/fb81981795d54efd738b_20200305152518034.png"

videoURL = "https://tvetamovie.pstatic.net/libs/1278/1278933/06db128921ea33bcd315_20200309104832664.mov-pBASE-v0-f99972-20200309105208281.mp4"

savePath1 = "c:/naver_ad.png"
savePath2 = "c:/naver_ad.mp4"

req.urlretrieve(imgURL, savePath1)

f = req.urlopen(videoURL).read()
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f)



