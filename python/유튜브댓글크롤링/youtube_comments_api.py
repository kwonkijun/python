import pandas
from googleapiclient.discovery import build

API_KEY = "AIzaSyB9udQ0F_92jazB1_sVjXLhIUC9MkTyFmE"
VIDEO_ID = "yQ20jZwDjTE"

comments = []
api = build('youtube', 'v3', developerKey=API_KEY)
response = api.commentThreads().list(part='snippet,replies', videoId=VIDEO_ID, maxResults=100).execute()

while response:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
 
        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
 
    if 'nextPageToken' in response:
        response = api.commentThreads().list(part='snippet,replies', videoId=VIDEO_ID, pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break

df = pandas.DataFrame(comments)
df.to_excel('api_result.xlsx', header=['comment', 'author', 'date', 'num_likes'], index=None)
