string = '오가니스트 오가니스트 키즈 샴푸 앤 바디워시 730ml 2in1 코스트코'
words = string.split(' ')

if(words[0] == words[1]):
	string = ' '.join(words[1:len(words)])

words = string.split(' ')

if(words[-1] == '코스트코'):
	string = ' '.join(words[0:len(words)-1])

print(string)