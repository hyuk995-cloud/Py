def print_double_line():
    print("\n"+"="*40+"\n")
    
def check_positive(number):
    if number > 0 :
        return True
    print("number < 0 일때 실행 확인용")
    return False

result = check_positive(10)
print(f"10은 양수? {result}")

result = check_positive(-5)
print(f"-5은 양수? {result}")

print_double_line() # ============================================

# BMI / 등급 함수
def calculate_bmi(weight, height):
    """ //독 스트링

    BMI 계산
    :param weight:체중(kg)
    :param height:키(cm)
    :return : BMI값(weight//((height/100)**2))
    """

    height_m = height/100
    bmi = weight/(height_m**2)
    return bmi

bmi = calculate_bmi(67, 177.7)
print(f"\n BMI : {bmi:.2f}")

def get_bmi_grade(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    else:
        return "비만"
    
grade = get_bmi_grade(bmi)
print(f"판정: {grade}")

user_weight = float(input("몸무게를 입력해주세요"))
user_height = float(input("몸무게를 입력해주세요."))
bmi = calculate_bmi(user_weight, user_height)
grade = get_bmi_grade(bmi)

print("\n === bmi 계산 결과 ===")
print(f"체중 {user_weight}kg")
print(f"키: {user_height}cm")
print(f"bmi:{bmi:.2f} ({grade})")


