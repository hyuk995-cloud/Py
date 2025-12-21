#로그인
user_id = "admin"
password = "1234"

if user_id == "admin" and password =="1234":
    print("로그인 성공")
    print(f"{user_id}관리자님 환영합니다.")
else:
    print("로그인 실패")
    

#할인대상 65세이상, 멤버쉽
age = 89
is_member = True

if age >= 65 or is_member:
    print("할인가능합니다.")
