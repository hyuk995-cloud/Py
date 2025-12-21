# ex1 ----------------------------------------------------
# 첫 번째 파이썬 연습
print(" Hello, World")
print("안녕하세요 반갑습니다.")
print("Python console 결과학인")
# --------------------------------------------------------

# ex2 ----------------------------------------------------
# print 기본
print("첫 번째 출력")
print("두 번째 출력")
# 줄바꿈 처리 없이 출력하기
print("첫 번째", end=" ")
print("두 번째")
# 여러 결과 값을 한 번에 출력하기
print("이름:","김철수","나이:",27,"살")
# ----------------------------------------------------------

# ex3-------------------------------------------------------
# 변수 선언과 대입
name = "홍길동"
age = 35
height = 182.5
is_student = True

# 변수 출력하기
print(name)
print(age)
print(height)
print(is_student)

# 변수와 문자 출력(복수)
print("이름 : ", name)
print("나이 : ", age, "세")
print("키 : ", height, "cm")
print("학생 여부 : ", is_student)

# 변수값 갱신 - 새로 정의
name = "김 철 수"
age = 25
height = 175.4
print()
print("이름 : ", name)
print("나이 : ", age, "세")
print("키 : ", height, "cm")
print("학생 여부 : ", is_student)
# ----------------------------------------------------------

# ex4-------------------------------------------------------

# 정수 변수 선언
a = 10
b = 3
print("더하기 : ", a + b)
print()
print("빼기 : ", a - b)
print()
print("곱하기 : ", a * b)
print()
print("나눗셈 : ", a / b)
print()
print("몫 : ", a // b )
print()
print("나머지 : ", a % b)
print()
print("거듭제곱 : ", a ** b)
print()

# 실수형 연산
pi = 3.14159
radius = 5
area = pi * radius ** 2
print("원의 넓이 : ", area)
print()

# 복합 대입 연산
x = 10
x += 7 # x = x + 7을 줄여서 x += 7
print(" x : ", x)
print()

x *= 3
print("x : ", x)
print()

x = x ** 2 # 에러나는 상황 : 문자열로 인식됨(위에 프린트 명령어 사용해서)
# [ x= int(x), float() ]
print("x : ", x)

# -------------------------------------------------------

# ex5 
# 자료형 확인
num_int = 100
num_float = 3.1415
text = "Python"
flag = True

print(type(num_int))
print(type(num_float))
print(type(text))
print(type(flag))

# 형 변환(type casting)
a = 10
b = str(a)
print(b, type(b))
c = "20"
d = int(c)
print(d, type(d))
e = int(num_float)
print(e, type(e))
# -----------------------------------------------------


# ex6--------------------------------------------------------
# 비교 연산자
age = 20
print(age > 18)
print(age >= 20)
print(age < 30)
print(age <= 19)
print(age == 20)
print(age != 25)

# 논리, 부정연산자
has_license = True
print(not has_license)

# 복합조건 파이썬만의 특징
score = 87
print(score>=80 and score < 90)
print(80<=score<90)
# ----------------------------------------------------------

# ex7
# 문자열 변수 선언(생성)
greeting = "안녕"
name = '파이썬'
message = """여러 줄
문자열을
만들 수 있습니다."""
print(greeting)
print(name)
print(message)


# 문자열 연결
name_greeting = greeting+" "+name
print(name_greeting)


#문자열 반복
echo = "하"*3
print(echo)


#문자열 길이(length)
text = "Programing"
length = len(text)
print("문자열 길이", length)
print(f"문자열 길이 : {length}") # 권장 형태 f"문자 {변수}"

#문자열 포함 여부
sentense = "Python is awesome"
print("Python" in sentense )
print("java" in sentense )
print("java" not in sentense )

# ------------------------------------------------------------
# ex8
# 개별문자 접근(인덱싱)
text = "Python"
print(text[0]) #P
print(text[1]) #y
print(text[5]) #n
print(text[-1]) #n
print(text[-2]) #o

# 슬라이싱(부분 문자 출력)
text = "Hello World"
print(text[0:5]) # 0~4인덱스 추출 Hello
print(text[6:11]) # 6~ 10까지 인덱스 world
print(text[:5]) #처음부터 4번까지
print(text[6:]) #6번 부터 끝까지
print(text[::2]) #2칸씩 출력
print(text[::-1]) #dlroW olleH

# 주민등록번호에서 생년월일, 성별코드 추출
text = "123456-123456"
so_num = "900102123456"
birth_date = so_num[:6]
gender_code = so_num[6]
print(f"생년월일 : {birth_date}")
print(f"성별코드 : {gender_code}")


# ------------------------------------------------------------
# ex9
#대소문자 변환
text = "HElLow python"
print(text)
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print()

#공백제거
message = " search words "
print(message) #" search words "
print(message.strip()) #"search words"
print(message.lstrip()) #"search words "
print(message.rstrip()) #" search words"

# =---------------------------------------------------------------
# ex 10

#문자열 검색
sentence ="Python is powerful ans Python is easy"
print(sentence.find("Python"))
print(sentence.find("java"))
print(sentence.index("Python"))
print(sentence.index("powerful"))
print(sentence.count("Python"))
print(sentence.startswith("Python"))
print(sentence.endswith("difficult"))
# ------------------------------------------------------------------
# ex 11
#문자열 분리(split)
fruit = "apple,banana,orange"
fruits = fruit.split(",")
print(fruits)
text="Python Programing Guide"
words=text.split()
print(words)

#문자열 결합(join)
favorite = "-".join(fruits)
print(favorite)

#문자열 치환(replace)
text="Easy Javascript, Python is good"
new_text = text.replace("Javascript","ECMA script")
print(new_text)

#제한 문자 치환
txt="aaa bbb ccc aaa ddd aaa"
new_txt = txt.replace("aaa","sss",2)
print(new_txt)

#문자 정렬
m_txt = "Python"
print(f"|{m_txt:<10}|") #왼쪽 정렬 (<10 == 폭을 10글자로 설정)
print(f"|{m_txt:>10}|") #오른쪽 정렬
print(f"|{m_txt:^10}|") #가운데 정렬