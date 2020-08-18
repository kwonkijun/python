# 확인문제
output = []
def flatten(data):
	global output
	for item in data:
		print(item)
		if type(item) == list:
			flatten(item)
		else:
			output.append(item)
	return output

example = [[1,2,3],[4,[5,6]], 7, [8,9]]

print("변환", flatten(example))