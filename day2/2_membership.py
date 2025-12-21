# 사용자 입력 - 정보 처리
user_input = " Kim Chul soo "
email = "kim@google.com"
phone = "010-1234-5678"

# 이름 정리( 공백제거, 대문자 변환)
name = user_input.strip().upper() # chain method .으로 이어져서 메서드를 적는것
print(f"정리된 이름 : {name}")

# 이메일( 아이디, 도메인 분리 )
email_parts=email.split("@") #["kim", "google.com"]
user_id = email_parts[0]
domain = email_parts[1]
print(f"아이디 : {user_id}")
print(f"도메인 : {domain}")
clean_phone = phone.replace("-","")
print(f"전화 번호 : {clean_phone}")
masked_phone=phone[:9]+"****"
print(f"마스킹 번호 : {masked_phone}")