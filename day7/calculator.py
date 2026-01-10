def input_float(prompt):
    """
    실수 입력 검증 함수
    
    """
    while True:
        try:
            return float(input(prompt)) #실수 변환 시도
        except ValueError:
            print("올바른 숫자를 입력하세요.")

# 재사용 여부 판단 Y / N 입력처리 함수
def input_yes_no(prompt):
    """예 아니오 입력함수"""
    while True:
        answer = input(prompt + "(Y/N)").upper()
        if answer in ["Y","N"]:
            return answer == "Y"
        else:
            print("Y 또는 N을 입력하세요.")

def calculator():
    """
    사칙연산 계산기 프로그램 함수
    1. 숫자1 입력
    2. 연산자 입력(+,-,*,/)
    3. 숫자2 입력
    4. 결과 출력
    """
    print("===== 계산기 =====")
    num1 = input_float("첫 번째 숫자 입력: ")
    print("사용가능 연산자 : *, /, +, -")
    operator = input("연산자 : ")
    num2 = input_float("두 번째 숫자 입력: ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("0으로 나눌 수 없습니다.")
            return
        result = num1 / num2
    else:
        print("올바른 연산자가 아닙니다.")
        return
# 결과 출력
    print(f"\n{num1}{operator}{num2} = {result}")

#calculator() 1회 실행

while True:
    calculator()
    
    if not input_yes_no("계속 계산하시겠습니까?"):
        break

    print("===== 계산기 종료 =====")