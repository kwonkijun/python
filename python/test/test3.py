products_no_opt=[
	['피지 파워 시트 세탁세제 120매 종이세제', 1, ''],
	['피지 파워 시트 세탁세제 120매 종이세제', 1, ''],
	['넬리 소다세제 3.29kg 세탁세제 아기세제 코스트코', 2, ''],
	['넬리 소다세제 3.29kg 세탁세제 아기세제 코스트코', 2, '']
]

products_opt =[
    ['오가니스트 키즈 샴푸 앤 바디워시 730ml 2in1', 2, '파우더향 730ml'],
    ['오가니스트 키즈 샴푸 앤 바디워시 730ml 2in1', 1, '복숭아향 730ml'],
    ['오가니스트 키즈 샴푸 앤 바디워시 730ml 2in1', 1, '복숭아향 730ml'],
    ['오가니스트 키즈 샴푸 앤 바디워시 730ml 2in1', 1, '복숭아향 730ml'],
    ['오가니스트 키즈 샴푸 앤 바디워시 730ml 2in1', 1, '복숭아향 730ml'],
    ['오가니스트 키즈 샴푸 앤 바디워시 730ml 2in1', 2, '파우더향 730ml'],
    ['오가니스트 키즈 샴푸 앤 바디워시 730ml 2in1', 2, '파우더향 730ml'],
	['스위스미스 핫코코아 믹스 핫초코 마시멜로', 1, '마쉬멜로'],
	['스위스미스 핫코코아 믹스 핫초코 마시멜로', 1, '밀크초콜렛']
]

cal_products_no_opt = []
cal_products_opt = []

cal_product_total = []

# 옵션 없는 상품 계산
for product in products_no_opt:
	exist = False
	for cal_product in cal_products_no_opt:
		if(product[0] == cal_product[0]):
			cal_product[1] += product[1]
			exist = True
	if(exist is False):
		cal_products_no_opt.append(product)


# 옵션 있는 상품 계산
for product in products_opt:
	exist = False
	for cal_product in cal_products_opt:
		if(product[0] == cal_product[0] and product[2] == cal_product[2]):
			cal_product[1] += product[1]
			exist = True
	if(exist is False):
		cal_products_opt.append(product)

for item in cal_products_no_opt:
	cal_product_total.append(item)

for item in cal_products_opt:
	cal_product_total.append(item)

print(cal_product_total)