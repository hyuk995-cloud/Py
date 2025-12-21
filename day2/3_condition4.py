temp = 35
print(f"현재 온도: {temp}도")

if temp >= 35:
    print("폭염 주의보!!!")
    print("야외 할동을 자제하세요.")

elif temp >= 30:
    print("무더운 날씨입니다.")
    print("실내 운동 주의")

elif temp >= 25:
    print("더운 날씨 입니다")
else:
    print("25이하 선선한 날씨입니다.")

print("날씨 확인 완료")

