import requests

params = {
    'pageNo' : 1,
    'rageType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : "파이썬"
}

response = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=params)

print(response.status_code)
print(response.url)