# 1~100 사이 숫자 맞추기 (시도 7번)
import random # random 모듈 불러오기

target = random.randint(1,100) # 1~100 사이 랜덤
tryNum = 0
max_try = 7
print("==== 숫자 맞추기 게임 ====")
print("1부터 100사이 숫자 맞추기")

while tryNum < max_try:
    userNum = int(input("숫자를 입력해주세요 1~100\n"))
    tryNum += 1
    if userNum == target:
        print(f"정답입니다. {tryNum}번 만에 맞추셨습니다.")
        break
    elif userNum < target:
        print("입력한 숫자보다 더 큰 숫자입니다.")
    else: # userNum > target
        print("입력한 숫자보다 작은 숫자 입니다.")
else: #while문이 break 없이 정상 종료시( 남은 기회 없음 )
    print(f"실패! 정답은 {target}")