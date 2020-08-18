import urllib.request as req
imgUrl = "https://ssl.pstatic.net/tveta/libs/1279/1279525/fb81981795d54efd738b_20200305152518034.png"
htmlURL = "http://google.com"

savePath1 = "c:/test1.jpg"
savePath2 = "c:/index.html"

f = req.urlopen(imgUrl).read()
f2 = req.urlopen(htmlURL).read()

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)
# with 구문을 빠져나오면서 리소스를 자동으로 반환한다. 

print("다운로드 완료!")