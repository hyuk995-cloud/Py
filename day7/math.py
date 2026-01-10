import math

#원 넓이, 둘레
radius = float(input("원의 반지름을 입력하세요: "))

area = math.pi*math.pow(radius,2) # 원주율(파이)*(반지름제곱)
circumference = 2*math.pi*radius
print(f"원의 넓이: {area:.2f}")
print(f"원의 둘레: {circumference:.2f}")

print("="*30)

#피타고라스의 정으리 = 빗변제곱 == 양변 제곱의 합
line1 = float(input("첫 번째 변의 길이: "))
line2 = float(input("두 번째 변의 길이: "))
line3 = math.sqrt(math.pow(line1, 2)+math.pow(line2,2))

print(f"빗변의 길이: {line3:.2f}")

print("="*30)

degree = 90
radian = math.radians(degree)

print(f"{degree}도 = {radian:.4f} 라디안")

sin_value = math.sin(radian)
print(f"sin({degree})도 = {sin_value:.4f}")