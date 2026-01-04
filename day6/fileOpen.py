import os
#===테스트 파일 생성, 작성 연습
with open("test.txt","w",encoding="utf-8") as file:
    file.write("수고 많으셨습니다.\n")
    file.write("파이썬 파일 처리 연습중입니다.\n")
    file.write("여러줄 확인중입니다.")



# try:
#     with open("test.txt","r",encoding="utf-8") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("파일을 찾을 수 없습니다.")

print("\n"+"="*40+"\n")#=====================================================

try:
    with open("test.txt","r",encoding="utf-8") as file:
        content1 = file.read(5) #처음 10자만 읽기
        content2 = file.read(5) # 다음 5자
        print(f"{content1}, {content2}")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

file_size = os.path.getsize("test.txt")
print(f"문서파일 크기: {file_size} bytes")

with open("test.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line :
            break
        print(line, end="")


with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readline()


empty_line = [line.strip() for line in lines]
print("줄바꿈 제거 리스트")
print(empty_line)