"""
파일 종류
- 텍스트 파일 : 텍스트에디터로 열 수 있습니다.
- 바이너리 파일 : 텍스트에디터로 열 수 없습니다.(이미지, 동영상, 워드, 엑셀, PDF 등)

파일 처리 방법
- 읽기(read) : r
- 쓰기
	- 새로(write) : w
	- 파일 뒤에 첨부(append) : a
"""

file = open('test.txt', 'a')
file.write('안녕하세요')
file.close()

# 위 세줄과 아래 세줄은 완전히 동일합니다.
with open('test.txt', 'a') as file:
	file.write('안녕하세요')

file = open('test.txt', 'r')
print(file.read())
file.close()

