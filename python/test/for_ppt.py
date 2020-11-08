import datetime

publish_year = int('2019')
publish_mon = int('09')
# 3달 이상 포스팅 안했을 경우 
date = datetime.datetime.today()
now_year = date.year
now_mon = date.month

if(now_year == publish_year):
	if(now_mon - publish_mon >= 3):
		print("삭제")
else:
	print("삭제")