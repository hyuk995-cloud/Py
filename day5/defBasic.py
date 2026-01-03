def print_double_line():
    print("\n"+"="*40+"\n")

def greet():
    print("="*30)
    print("안녕하세요.")
    print("환영합니다!")
    print("="*30)

greet()

def print_start():
    for i in range(5):
        print("*"*(i+1))


print("별 찍기 ===")
print_start()

print_double_line()

def greet_person(name):
    print(f"안녕하세요... {name}님")

greet_person("김철수")
greet_person("오영희")
greet_person("박만수")
print_double_line()

def create_user(name, age, city):
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"도시: {city}")

create_user("서새봄",31,"서울")
print_double_line()

def show_product(name,price,stock):
    print("\n==== 제품정보 ===")
    print(f"상품명: {name}")
    print(f"가격: {price:,}원")
    print(f"재고: {stock:,}개")

show_product(
    name = "노트북",
    price = 12000000,
    stock = 3000
)

show_product(
    name = "마우스",
    price = 8000,
    stock = 12500
)

print_double_line()
#매개변수 기본값
def create_account(username, password="1234", level="일반"):
    print(f"계정 생성: ")
    print(f" 아이디 : {username}")
    print(f" 비밀번호 : {password}")
    print(f" 등급 : {level}")

create_account("user1")
create_account("user2", "3456")
create_account("admin", "asdf", "관리자")
create_account("vip",level="VIP")

print_double_line()

#가변매개변수
def print_numbers(*numbers):
    print(f"받은 인자 개수: {len(numbers)}") 
    print(f"타입 : {type(numbers)}") #tuple
    for num in numbers:
        print(num, end=" ")
    print()

print_numbers(1,2,3)
print_numbers(1,2,3,4,5)
print_numbers(9)

#합계
def calculate_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"\n 1+2+3 = {calculate_sum(1, 2, 3)}")
print(f"\n 1+2+3+4+5 = {calculate_sum(1, 2, 3, 4, 5)}")
print(f"\n 10+20+30 = {calculate_sum(10, 20, 30)}")
print_double_line()

#평균
def calculate_average(*scores):
    if len(scores)==0:
        return 0
    total = sum(scores)
    return total/len(scores)

print(f"\n평균 :{calculate_average(100,95,88):.2f}")
print_double_line()

def create_team(leader, *members):
    print(f"팀장 : {leader}")
    print(f"팀원 : {', '.join(members)}")

create_team("홍길동", "김철수", "유재석", "강호동")

print_double_line()

def create_profile(name, **details):
    print(f"\n===={name}의 프로필====")
    for key, value in details.items():
        print(f"{key}: {value}")

create_profile(
    "고길동",
    age=22,
    major="컴퓨터공학과",
    hobby="코딩",
    city="인천"
)
create_profile(
    "유재석",
    age=30,
    major="개그과",
    hobby="mc",
    city="서울"
)

print_double_line()

def create_order(customer, *items, **options): #docstring """ 설명 """
    """
    create_oder의 docsring
    주문 생성 함수    
    :param customer : 고객명
    :param items : 주문상품들
    :param option :  추가옵션들
    """
    print("=n"*40)
    print(f"고객: {customer}")
    print(f"\n 상품목록:")
    total = 0
    for i, item in enumerate(items, 1):
        print(f" {i}.{item} ")
    print("\n옵션:")
    for key, value in options.items():
        print(f"{key}: {value}")
        
    print("\n 주문완료")

    create_order(
        "김철수",
        "아메리카노",
        "바닐라라떼",
        "샌드위치",
        payment = "카드",
        delivery = "매장",
        note = "얼음은 많이"
    )

    create_order(
        "이영희",
        "에스프레소",
        payment = "현금"
    )