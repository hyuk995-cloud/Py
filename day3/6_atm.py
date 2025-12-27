# 비밀번호 확인 -> 메뉴 선택 -> 거래

balance = 10000 #잔액
password = "1234" #비밀번호

is_login = False
tryNum = 0

while tryNum < 5:
    user_password = input("비밀번호를 입력해주세요.")
    tryNum += 1

    if user_password == password:
        print("인증")
        is_login = True
        break
    else:
        remain = 5 - tryNum
        if remain > 0:
            print(f"비밀번호가 틀렸습니다. 남은 횟수 {remain}번")
        else:
            print("로그인 실패! 프로그램이 종료 됩니다.")

if not is_login:
    print("ATM 종료")
else:
    running = True
    
    while running:
        print(f"\n 현재 잔액: {balance:,}원")
        print("1. 입금")
        print("2. 출금")
        print("3. 잔액조회")
        print("4. 종료")
        choice = input("원하는 메뉴를 선택하세요. : ")
        if choice == "1" :
            amount = int(input("입금할 급액을 입력하세요. "))
            balance += amount
            print(f"\n {amount:,}원을 입금했습니다. 현재 금액{balance:,}")
        elif choice == "2" :
            amount = int(input("출금할 금액을 입력하세요 : "))
            if amount <= balance:
                balance -= amount
                print(f"{amount:,}원이 출금 되었습니다. 현재 금액{balance:,}")
            elif amount > balance:
                print("잔액이 부족합니다.")
        elif choice == "3" :
            print(f"현재 잔액 : {balance:,}원 입니다.")
        elif choice == "4" :
            print("이용해주셔서 감사합니다.")
            running = False
            break
        else: # 1~4가 아닌 다른 문자를 입력 했을 경우
            print("잘못된 값을 입력했습니다. 다시 1~4까지의 숫자를 입력하세요.")

print("\n atm 종료 ---")