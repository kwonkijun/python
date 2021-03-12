import re
test_string = 'ㅊㄱㅍ<a href="https://www.youtube.com/watch?v=yQ20jZwDjTE&amp;t=1h11m55s">1:11:55</a>'

print(re.search('</a>', test_string))
