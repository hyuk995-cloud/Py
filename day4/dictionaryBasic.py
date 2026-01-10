#딕셔너리 생성
student = {
  "name":"김철수",
  "age":28,
  "job":"developer",
  "grade":"대리"
}
print(student)
print(f"이름 : {student['name']}")
print(f"나이 : {student['age']}")
print(f"직업 : {student['job']}")
print(f"직급 : {student.get('grade')}")
# 빈 딕셔너리 생성
empty1 = {}
empty2 = dict()

print("\n"+"="*40+"\n")

person = {
  "name":"홍길동",
  "age":29,
  "height":185.3,
  "hobbies":["독서","영화","운동"],
  "address":{
    "city":"인천",
    "district":"남동구"
  },
  "is_Student":True
}
print(person)
print("\n"+"="*40+"\n")
print(f"이름: {person['name']}")
print(f"취미들: {person['hobbies']}")
print(f"첫번째 취미: {person['hobbies'][0]}")
print(f"사는 도시: {person['address']['city']}")

#  print(student['phone'])   존재하지 않은 키 호출시 keyError
#  get()로 존재하지 않은 키 호출시  'none'반환 , 없는 키 일 경우 기본값 정의 가능
result = person.get('phone')
print(f"전화 번호: {result}")
result = person.get('phone','등록하지 않음')
print(f"전화 번호: {result}")

#기존 갑 수정
person['age'] = 27
#데이터 추가
person['gender'] = '남자'
print(person)
#여러 데이터 추가(수정) -- 두번 지정, update() 활용 - 추가,수정 
#person['phone'] = "010-1234-5678"
#person['email'] = "hong@ex.com"
person.update({
  'height':184,
  'phone':'010-5678-9876',
  'email':'hong@ex.com',
  'major':'컴퓨터공학'
})
print(person)
# setdefault() 해당 추가데이터가 없을때만 추가 , 존재시 추가 안됨
person.setdefault('major','경영학')  # 추가 안됨
person.setdefault('club','코딩동아리')  # 새로 추가
print(person)

print("\n"+"="*40+"\n")

# 철자 카운트
text = "hello world"
char_count = {}

for char in text:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1
print(f"문자 카운드 : {char_count}")
char_count2 = {}

for char in text:
  char_count2[char] = char_count2.get(char,0)+1
print(f"문자 카운드 : {char_count2}")

print("\n"+"="*40+"\n")
# person 딕셔너리 데이터 삭제
#del dict[key] -- 제거
del person['gender']
print(f"성별 데이터 삭제: {person}")
# pop(key) : 삭제, 값 반환
remove_item = person.pop('club')
print(f"삭제 데이터 : {remove_item}")
print(f"pop() 실행 후 : {person}")
#기본값 정의로 에러없이 삭제 pop(key,'default')
# person.pop('credit')  error
remove_value = person.pop('credit','없음')
print(f"삭제 데이터 : {remove_value}")

#전체 삭제 : clear()
person_copy = person.copy()   #복제
print(f"복사본 : {person_copy}")
person_copy.popitem()
print(f"popitem실행 결과 : {person_copy}")
person_copy.clear()
print(f"복사본 clear실행 : {person_copy}")
#popitem() -- 마지막 항목 삭제    dict.popitem()