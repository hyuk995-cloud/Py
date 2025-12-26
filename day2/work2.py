# 과제2.
user_height = input("키를 입력해주세요.")
user_age = input("나이를 입력해주세요.")
user_height.strip()
user_age.strip()
age = 10
height = 140
if user_height.isdigit() and user_age.isdigit():
    user_height = int(user_height)
    user_age = int(user_age)
    scarce_height = height - user_height
    scarce_age = age - user_age
    print(f"당신의 나이는 : {user_age}, 당신의 키는 : {user_height} 입니다.")
    if user_height >= height and user_age >= age :
        print("놀이기구를 탑승할 수 있습니다.")
    elif user_height >= height and user_age < age:
        print(f"탑승할 수 없습니다 : 나이 부족, 나이{scarce_age}세 더 먹고 오세요.")
    elif user_height < height and user_age >= age:
        print(f"탑승할 수 없습니다 : 키 부족, 키{scarce_height}cm 더 크고 오세요.")
    else:
        print(f"탑승할 수 없습니다. : 키 부족({scarce_height}cm), 나이 부족({scarce_age}세)")
else:
    print("올바른 숫자를 입력해주세요.")
    