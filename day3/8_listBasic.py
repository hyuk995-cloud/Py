numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fruits = ["apple", "orange", "banana"]
mixed = [1, "text", 3.14, True]
empty = []

# 인덱싱
print("\n"+"="*40+"\n")

print(f"첫 번째 : {fruits[0]}")
print(f"두 번째 : {fruits[1]}")
print(f"마지막 번째 : {fruits[-1]}")
print(f"뒤에서 두 번째 : {fruits[-2]}")

print("\n"+"="*40+"\n")

# 슬라이싱
print(f"0 ~ 4번 : {numbers[0:5]}")
print(f"5번 ~ 끝 : {numbers[5:]}")
print(f"처음부터 3번 : {numbers[:4]}")
print(f"전체 : {numbers[:]}")
print(f"두칸씩 출력 : {numbers[::2]}") # 0 2 4 6 8
print(f"역순 : {numbers[::-1]}") # 9 8 7 ... 0

print("\n"+"="*40+"\n")

# 리스트
print(f"fruits리스트 길이 : {len(fruits)}") # fruits 리스트의 길이 : 3
print("\n"+"="*40+"\n")

# 리스트 수정 fruits = ["apple", "orange", "banana"]
fruits[1] = "grape" # 오렌지 사라지고 포도로 바뀜
print(f"두번째 자리 교체 오렌지 -> 포도 {fruits}")
print("\n"+"="*40+"\n")

# text = "abc"
# text[0] ="z" # 불가능  (문자 <--> 리스트로 바꿔야 변환 가능)

#슬라이싱으로 여러요소 수정
numbers[1:4] = [20, 30, 40]
print(f"슬라이싱 수정 : {numbers}")

print("\n"+"="*40+"\n")

#리스트 연산
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combine = list1 + list2
print(f"연결 : {combine}")

pattern = [7, 8]*3
print(f"반복 패턴 : {pattern}") # [7, 8, 7, 8, 7, 8] -- 리스트 값 초기화시 유용(게임 순위 같은데에서 사용)

print("\n"+"="*40+"\n")

# 포함 여부 확인( in, not in )
print(f"'apple' in fruits : {'apple' in fruits}") # 리스트에 사과가 있니?
print(f"'orange' in fruits : {'orange' in fruits}") # 리스트에 오렌지가 있니?
print(f"'orange' not in fruits : {'orange' not in fruits}") # 리스트에 오렌지가 없니? (조건문 활용)

print("\n"+"="*40+"\n")

# 리스트 비교( ==, <, > )
lists1 = [1, 2, 3]
lists2 = [1, 2, 3]
lists3 = [1, 2, 4]

print(f"{lists1} == {lists2} : {lists1 == lists2}")
print(f"{lists1} == {lists3} : {lists1 == lists3}")
print(f"{lists1} < {lists3} : {lists1 < lists3}") # 배열 개수가 서로 맞아야만 가능, 하나라도 틀리면 오류된 값을 출력함

print("\n"+"="*40+"\n")
