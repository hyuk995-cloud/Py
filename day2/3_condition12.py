# 자판기 콜라 1500, 쥬스 2000, 생수 1000

cola_price = 1500
juice_price = 2000
water_price = 1000

money = input("투입할 금액을 입력하세요 : ")
money = int(money)
choice = input("음료를 선택하세요.(콜라, 쥬스, 생수) : ")

print(f"투입 금액은 : {money:,}원")
print(f"선택 {choice}")
if choice =="콜라" or choice =="cola":
    price = cola_price
elif choice == "주스" or choice == "쥬스" or choice == "juice":
    price = juice_price
elif choice =="생수" or choice == "water":
    price = water_price
else :
    print("없는 상품입니다.")
    price = 0

if price > 0:
    if money >= price:
        print(f"\n{choice}가 나왔습니다.")
        change = money - price
        print(f"거스름돈 : {change:,}원")
    else:
        shortage = price - money
        print("\n금액이 부족합니다.")
        print(f"{shortage:,}원이 필요합니다.")