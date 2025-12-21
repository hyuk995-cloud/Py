#BMI(체질량지수)
height = 180
weight = 65
print(f"키 : {height}cm")
print(f"몸무게 : {weight}kg")


#계산
height_m = height/100
bmi = weight/(height_m*height_m)
print(f"BMI : {bmi:.1f}")

#판정 결과 출력
if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("정상")
elif bmi < 25:
    print("과체중")
else:
    print("비만")
    
# 3,4,5 봄 6,7,8 여름 9,10,11 가을 12,1,2 겨울
m = input("월을 입력하세요 : ")
m = int(m)
if m == 12 or m == 1 or m == 2:
    print("겨울")
elif 3<=m<=5:
    print("봄")
elif 6<=m<=8:
    print("여름")
elif 9<=m<=11:
    print("가을")
else:
    print("올바른 숫자를 입력해주세요 1~12")

