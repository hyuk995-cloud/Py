#튜플 생성
numbers = (1,2,3,4,5)
fruits = ("사과","배","바나나")
mixTuple = (1, "text", 3.14, True)
print(f"숫자 튜플: {numbers}")
print(f"과일 튜플: {fruits}")
print(f"혼합 튜플: {mixTuple}")
#괄호 생략 가능
coordinates = 10.34344, 35.147
print(f"좌표 : {coordinates}")
#요소 하나일 경우는 쉼표필수 입력
singleTuple = (1,) # 튜플 생성
singleVar = (1) # 정수입력
print(f"singleTuple 타입: {type(singleTuple)}")
print(f"singleVar 타입: {type(singleVar)}")
#빈 튜플
empty = ()
print(f"빈 튜플 : {empty}")
#슬라이싱 호출 가능, 연산가능(+) -> 새튜플생성
print(f"첫 번째: {numbers[0]}")
print(f"마지막 번째: {numbers[-1]}")
print(f"슬라이싱[1:4]: {numbers[1:4]}") #2,3,4
print(f"슬라이싱[:3]: {numbers[:3]}") #1,2,3
print(f"슬라이싱[3:]: {numbers[3:]}") #4,5
#부분수정,삭제 안됨  전체 삭제만 가능
del numbers
tuple1 = (1,2,3)
tuple2 = (4,5,6)
combine = tuple1+tuple2
print(f"연결: {tuple1}+{tuple2} = {combine}")
repeated = tuple1*3
print(f"반복:{tuple}x3 = {repeated}")
print(f"tuple1 길이: {len(tuple1)}개")
print(f"2 in {tuple1}: {2 in tuple1}")
print(f"8 in {tuple2}: {8 in tuple2}")
# sum(), max(), min() 도 가능

# 리스트 와 튜플 변환
myList = [1,2,3,4,5]
myTuple = tuple(myList)  
print(f"리스트:{myList} >>> 튜플:{myTuple}")
myTuple2 = (10,20,30)
myList2 = list(myTuple2)
print(f"튜플:{myList2} >>> 리스트:{myTuple2}")
text = "python"
char_tuple = tuple(text)
print(f"문자열 : '{text}' >>> 튜플:{char_tuple}")
# 검색 - 요소개수 count(), 위치찾기 index('data'), index('data',검색시작순번)
fruits = ("사과", "바나나", "딸기", "바나나", "사과")
appleCount = fruits.count("사과")
print(f"사과의 개수: {appleCount}")
index = fruits.index("바나나")
print(f"바나나의 인덱스(처음): {index}")
index2 = fruits.index("바나나",2)
print(f"바나나의 세번째부터 검색결과: {index2}")

print("\n"+"="*40+"\n")
# 언패킹
point = (10,20)
x,y = point
# 튜플 값을 각 변수에 할당
print(f"x = {x}, y = {y}")

name, age, city = ("이영희",25,"인천")
print(f"\n이름: {name}")
print(f"나이:{age}")
print(f"도시:{city}")

a=10
b=20
a, b = b, a
print(f"교환 결과: a={a}, b={b}")
