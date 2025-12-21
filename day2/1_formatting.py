# %포매팅
name = "홍길동"
age = 35
height = 178.3
print("이름 : %s, 나이 : %d세, 키 : %.1fcm" % (name, age, height))
pi = 3.14359235
print("파이 : %.2f" % pi) # 소수점 2자리

# format()
name = "김철수"
age = 27
print("이름 : {}, 나이 : {}".format(name, age))
print("이름 : {0}, 나이 : {1}, 이름 확인:{0}".format(name, age))
print("이름 : {n}, 나이 : {a}".format(n=name, a=age))

# f-string
name = "이영희"
age = 28
height = 168.3
print(f"이름 : {name}")
print(f"나이 : {age}세")
print(f"키 : {height}cm")
price = 12345678
print(f"가격 : {price:,}원")
pi = 3.141592
print(f"원주율 : {pi:2f}")

# 2진수 {변수명:b} , 16진수 {변수명:x}