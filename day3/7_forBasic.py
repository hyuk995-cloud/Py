#for 기초 범위설정 ( range() )
for i in range(7):
    print(f"{i+1}번째 실행 확인")

print("="*20)

for i in range(1, 11): # 1 ~ 10까지
    print(i, end=" ")
print("\n"+"="*20)

for i in range(0, 10, 2):# 0~10까지 2씩 증가
    print(i, end=" ")
print("\n"+"="*20+"\n")

for i in range(10, 0, -2): #역순
    print(i, end=" ")
print("\n"+"="*20+"\n")

text = "PythonText" # 문자열, text[0] --> "p"
for char in text:
    print(char)
print("\n"+"="*20+"\n")

text2 = "RangeIndex"
for i in range(len(text2)):
    print(f"{i}: {text2[i]}번 째 입니다.")
print("\n"+"="*20+"\n")

text3 = "Enumerate"
for index, char in enumerate(text3):
    print(f"{index}:{char}")

print("\n"+"="*20+"\n")
# 1~100 까지 합
total = 0
even_total = 0 #짝수
odd_total = 0 #홀수

for i in range(1, 101):
    total += i
    

for i in range(1, 101):
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i


print(f"1부터 100까지의 합은 {total} 입니다.")
print(f"1부터 100까지의 합은 {even_total} 입니다.")
print(f"1부터 100까지의 합은 {odd_total} 입니다.")
print("\n"+"="*20+"\n")

# 별 찍기

for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()
print("\n"+"="*20+"\n")