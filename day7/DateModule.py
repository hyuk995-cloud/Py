import datetime
#현재날짜, 시간


now = datetime.datetime.now()
print(now)

#날짜,시간
print(now.date())
print(now.time())

#특정날짜 선택
eventDay = datetime.datetime(2025,5,15)
print(eventDay)
year = int(input("년도 입력 : "))
month = int(input("월 입력)"))
day = int(input ("일 입력: "))


#d-day

dday = (eventDay-now).days

if dday> 0:
    print(f"D-{dday})남았습니다.")
elif dday == 0:
    print("D-day입니다!!!")
else:
    print(f"D+{abs(dday)} 지났습니다.")

# 나이계산
print("==========나이 계산 ============")
birth_year = int(input("태어난 년도 입력 : "))
birth_month = int(input("태어난 월 입력 : "))
birth_day = int(input("태어난 일 입력 : "))

birth_date = datetime.datetime(birth_year, birth_month, birth_day)

age_days = (now - birth_date).days
age_years = age_days // 365

print(f"태어난지 {age_days}일이 지났습니다.")
print(f"{age_years}세 이네요.")

#근무시간 기록기

start_time = datetime.datetime.now()
print(f"출근시간 : {start_time.strftime('%H:%M:%S')}")
input("퇴근시 Enter를 입력하세요.")
end_time = datetime.datetime.now()
print(f"퇴근시간 : {end_time.strftime('%H:%M:%S')}")

work_time = end_time - start_time
works_seconds = work_time.total_seconds()
work_hours = works_seconds // 3600
work_minutes = (works_seconds % 3600) // 60

print(f"총 근무 시간 : {int(work_hours)}시간 {int(work_minutes)}분")
