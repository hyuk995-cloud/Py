def input_int(prompt):
    """
    사용자가 올바른 정수 입력할 때 까지 반복
    작동원리
    1. 사용자에게 입력 요청
    2. int()변환 시도
    3. 성공하면 값 반환, 실패하면 다시 입력요청 (try 성공시 실행, except 에러종류 에러시 실행)
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("올바른 숫자를 입력하세요.")

age = input_int("나이를 입력하세요. : ")

print(f"입력된 나이 : {age}세")