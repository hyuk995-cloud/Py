hour = input("시간을 입력해주세요, ex) 1시간 -> 1, 2시간 -> 2, 30분 -> 0 ")
minute = input("분을 입력해주세요.")
hour.strip()
minute.strip()
# 30분 이하 2천원
# 30분 ~ 1시간 3천원
# 1시간 초과 3천원+시간당 천원
if hour.isdigit() and minute.isdigit():
    hour = int(hour) # 시간
    minute = int(minute) # 분
    hour_trans = hour * 60 # 유저가 입력한 시간을 변환
    over_hour = hour - 1
    time = hour_trans + minute # 변환된 시간 + 유저가 입력한 분을 합침
    price1 = 2000
    price2 = 3000
    add_price = 1000 #추가 비용
    
    if time >= 61: # 토탈 시간이 61분보다 클 경우
        total_price = price2+(int(time / 60) * add_price) # 추가비용 계산 식
        print(f"주차 비용은 다음과 같습니다, 주차 시간 {hour}시간 {minute}분, 초과 시간 {over_hour}시간 {minute}분, 추가 비용 {int(time / 60) * add_price}, 총 금액{total_price:,}입니다.")
    elif 30 < time <= 60:
        print(f"주차 비용은 다음과 같습니다. 주차 시간 {hour}시간 {minute}분, 주차 비용{price2:,}원 입니다.")
    
    else:
        print(f"주차 비용은 다음과 같습니다. 주차 시간 {hour}시간 {minute}분, 주차비는 {price1:,}원 입니다.")
else:
    print("올바른 시간을 입력해주세요.")