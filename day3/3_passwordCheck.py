admin_password = "1234"
count = 0
max_count = 3

while count < max_count:
    password = input("비밀번호 : ")
    count += 1

    if password == admin_password:
        print("로그인이 성공!")
        break
    else:
        remainCount = max_count - count
        if remainCount > 0:
            print(f"비밀번호가 틀렸습니다. 남은 횟수{remainCount}번")
        else:
            print("로그인 실패")

print("="*20)