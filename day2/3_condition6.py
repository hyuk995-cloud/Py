# 구매 3만원
# 5만원 이상 10% 할인, 배송비 무료
# 5만원 미만 배송비 3천원
# 5만원이 아닐 경우 차이만큼 구매하면 배송비 무료다 라고 표시

price = 30000 #구매 금액
minumum_price = 50000 #할인 기준 금액

print(f"구매 금액 : {price}원")

if price >= minumum_price:
    discount = price*0.1
    final_price = price - discount
    print(f"할인 적용 : {discount:,}원")
    print(f"배송비 무료")
    print(f"최종 금액 : {final_price:,}원")
else:
    print("할인 미적용")
    print("배송비 3000원")
    final_price2 = price + 3000
    print(f"최종 가격 : {final_price2:,}원")
    need_more = minumum_price - price
    print(f"{need_more:,}원 더 구매하면 10%할인과 배송비 무료")