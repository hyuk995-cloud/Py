# 사칙연산 계산기
print("="*10)
print("계산기")
print("="*10)

num1 = input("계산할 숫자를 입력하세요.")
num2 = input("계산할 두번째 숫자를 입력하세요.")
operator = input("연산자를 입력하세요.")

num1 = int(num1)
num2 = int(num2)

if operator == "+":
    result = num1+num2
    print(f"결과 : {result}")
    
elif operator == "-":
    result = num1-num2
    print(f"결과 : {result}")
    
elif operator == "*":
    result = num1*num2
    print(f"결과 : {result}")
    
elif operator == "/":
    if num2 == 0:
        print("오류 발생 : 0으로 나눌 수 없습니다.")
    else:
        result = num1/num2
        print(f"결과 : {result}")
else:
    print("오류발생: 올바른 연산자를 입력하세요.")


print(f"{num1} {operator} {num2} = {result}")