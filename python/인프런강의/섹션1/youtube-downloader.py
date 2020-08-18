from pytube import YouTube
import os
import subprocess

yt = YouTube("https://www.youtube.com/watch?v=_9FTyEbKFEM")
videos = yt.streams.all()

# range 함수 range(1,6) 1,2,3,4,5 range(6) 0,1,2,3,4,5

for i in range(len(videos)) : 
    print(i, ' , ', videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "c:/youtube"
videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

# 커맨드 명령어 실행 리스트 형태로 하나씩 넣는다. 
subprocess.call([
    'ffmpeg',
    '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName)
])

print("동영상 다운로드 및 mp3 변환 완료!")