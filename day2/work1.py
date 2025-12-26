# 과제1
c = input("온도를 입력해주세요.")
c.strip()
# print(c.isdigit()) 인풋이 숫자인지 아닌지 확인
if c.isdigit():
    c = int(c)
    f = (c*(9/5))+32
    print(f"섭씨 : {c}도, 화씨 : {f}도")
    if  c >= 86 or f >= 30:
        print("날씨가 덥습니다.")
    else:
        print("날씨가 적당합니다.")
else:
    print("올바른 숫자를 입력해주세요.")
# 과제3:
