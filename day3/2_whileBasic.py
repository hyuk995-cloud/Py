# == 구구단 8단 출력
dan = 8 #출력 단
i = 1 #구구단 숫자(곱하기)
print(f"===={dan}단=====")
while i <= 9:
    result = dan*i
    print(f"\n{dan} * {dan} x {i} = {result}")
    i+= 1
    print("="*20)

# === break
count = 1
while count <= 10:
    if count == 5:
        print("5에서 실행 중단!!!!")
        break
    print(count)
    count += 1
print("반복 종료 \n")

# === continue (1부터 10까지 홀수만 출력)
countNum = 0
while countNum < 10:
    countNum += 1
    if countNum % 2 == 0:
        continue    #아래코드 실행하지 않고 다음 반복
    print(countNum)

print("반복 종료 \n")

#무한 반복 1부터 증가 출력 3의 배수일 때 스킵(컨티뉴) 20 넘으면 종료
countUp = 0

while True:
    countUp += 1
    if countUp > 20:
        print("20초과로 종료")
        break
    if countUp % 3 == 0:
        continue

    print(countUp)