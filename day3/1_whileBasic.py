# 기본 while문 기초 --- 임의 변수 count가 1부터 5이하일 동안 반복되는 조건
count = 1
while count <= 5: #count 변수가 5이하일 동안만 반복
    print(f"{count}번째 실행")
    count += 1 # count 변수의 조건 접근식(증가식)
print("반복실행 종료")

#역 카운트

countdown= 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("카운트 다운 종료 0")

x = 10
while x < 5:
    print("실행확인")
    x += 10
    print("반복조건 충족 안됨: Fasle")

# 누적해서 더하기
total = 0 #합계 계산 변수
num = 1 #누적 증가 변수
while num <= 20:
    total += num
    print(f"num까지의 합: {total}") 
    num += 1
print(f"=,최종 합계 결과 : {total}")