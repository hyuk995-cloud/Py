import os
from datetime import datetime

#현재 위치 (프로젝트 폴더 경로) 확인
current_dir = os.getcwd()
print(f"현재 위치 : {current_dir} \n")

# 파일 목록 보기
print("파일 및 폴더 목록: ")
files = os.listdir(".")
for item in files[:20]:
    #파일, 폴더 구분
    path = os.path.join(".", item)
    if os.path.isdir(path):
        print(f"{item}/")
    else:
        size = os.path.getsize(path)
        print(f"{item} ({size:,} bytes)")