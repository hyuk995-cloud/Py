# 윤년 조건
# 4로 나누어떨어지고, 400년 마다 윤년, 100년마다 평년

year = input("숫자를 입력하세요 ")
year = int(year)

print(f"{year}년 윤년 확인 중")

if year % 400 == 0:
    print("윤년입니다.(400의 배수)")
elif year % 100 == 0:
    print("평년입니다. (100의 배수)")
elif year % 4 == 0:
    print("윤년입니다. (4의 배수)")
else:
    print("평년입니다.")
