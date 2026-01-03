# count(요소) - 요소 개수 파악
numbers = (1, 2, 3, 4, 5, 2, 4, 3, 2, 1)
count = numbers.count(2)
print(f"2의 개수: {count}개")

#index() - 요소 위치 찾기
index = numbers.index(5)
print(f"5의 순서 : {index+1}번째")

index2 = numbers.index(3)
print(f"첫 번째 3의 순서: {index+1}번째")

for num in numbers:
    print(num)

for i, num in enumerate(numbers):
    print(f"{i}:{num}")