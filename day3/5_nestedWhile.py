#2단 ~ 9단 구구단 출력 중첩 반복문
dan = 2

while dan <= 9:
    print(f"\n === {dan}단 === ")
    num = 1
    while num <= 9:
        print(f"{dan} x {num} = {dan*num}")
        num += 1
    dan += 1

print("="*20)