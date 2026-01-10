# 중첩 리스트( 2차원 리스트 )
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(f"matrix[0][0]: {matrix[0][0]}")  #1
print(f"\nmatrix[1][1]: {matrix[1][1]}")  #5
print(f"\nmatrix[2][2]: {matrix[2][2]}")  #9

#for 리스트 데이터 순환 - 요소 직접 요청
for row in matrix:
  print(row)

print("\n"+"="*40+"\n")

fruits = ["apple","banana","orange","grape"]
# 인데스로 순환 요청
for i in range(len(fruits)):
  print(f"{i}: {fruits[i]}")

print("\n"+"="*40+"\n")
#enumerate 사용
for index, fruit in enumerate(fruits):
  print(f"{index} : {fruit}")

print("\n"+"="*40+"\n")

#반복-- 리스트 데이터 생성 ( append() )
data = []
for i in range(1,11):
  data.append(i**2)
print(f"제곱수 data: {data}")

print("\n"+"="*40+"\n")
#일반 생성
numbers=[]
for i in range(1,6):
  numbers.append(i)

print("\n"+"="*10+"Comprehension"+"="*10+"\n")
#리스트 컴프리핸션
numbers_comp = [i**2 for i in range(1,6)]
print(f"numbers_comp: {numbers_comp}")
#조건문 추가 
even_numbers = [i for i in range(1,11) if i%2==0]
print(f"even_numbers: {even_numbers}")
print("\n"+"="*40+"\n")
#for 추가
colors = ["빨강","파랑"]
sizes = ["S", "M", "L"]
combines = [f"{size}_{color}" for color in colors for size in sizes]
print(f"combines: {combines}")

print("\n"+"="*40+"\n")

# 통계 - 내장함수( 숫자 합계:sum(~), 최대값:max(~), 최소값:min(~), 평균
scores = [27, 45, 13, 69, 36, 91, 16]
total = sum(scores)
maxScore = max(scores)
minScore = min(scores)
average = total/len(scores)
print(f"숫자 리스트 : {scores}")
print(f"합계 : {total}")
print(f"최대 : {maxScore}")
print(f"최소 : {minScore}")
print(f"평균 : {average:.2f}")

print("\n"+"="*40+"\n")

nums = [1,2,3,4,5,6,7,8,9,10]
gt5 = []
for n in nums:
  if n>5:
    gt5.append(n)

greater_than_5 = [n for n in nums if n>5]
