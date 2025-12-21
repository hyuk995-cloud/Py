#버스 비
age = 20
print(f"나이 : {age}세")

if age < 7:
    price = 0
    print("미취학 아동 무료")
elif age < 13:
    price = 300
    print(f"어린이 요금 :{price}원")
elif age < 19:
    price = 700
    print(f"청소년 요금 :{price}원")
elif age < 65:
    price = 1350
    print(f"성인 요금 :{price:,}")
else:
    price = 0
    print("경로 우대 무료")

print(f"버스요금 : {price:,}원")