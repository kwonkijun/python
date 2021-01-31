price_dic = {}

price_dic["2021/01/01"] = 85000
price_dic["2021/01/02"] = 86000
price_dic["2021/01/03"] = 87000
price_dic["2021/01/04"] = 84000
price_dic["2021/01/05"] = 85000

for key in price_dic.keys():
    print(key)

for value in price_dic.values():
    print(value)

for item in price_dic.items():
    print(item)