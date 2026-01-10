#append -- 리스트 마지막 위치에 요소 추가
fruits = ["사과","바나나"]
fruits.append("오렌지")
print(f"append 오렌지 결과: {fruits}")

fruits.append("포도")
print(f"append 포도 결과: {fruits}")

print("\n"+"="*40+"\n")
#insert -- 지정 위치에 요소 삽입(추가)
fruits.insert(1, "키위")
print(f"insert 1 키위 결과: {fruits}")

#remove 삭제  - 없는 데이터 삭제 요청히 valueError
fruits.remove('바나나')
print(f"remove 바나나 결과: {fruits}")

#pop 순번으로 삭제, 반환, pop()순서지정 없으면 마지막 요소 삭제
removeItem = fruits.pop(1)
print(f"pop 1 결과: {fruits}")
print(f"삭제한 과일: {removeItem}")

print("\n"+"="*40+"\n")

fruits.append("수박")
fruits.append("참외")
fruits.append("딸기")

print(f"새로 추가 과일들: {fruits}")
#del 순서나 슬라이스[start:end]형태로 삭제
del fruits[0]
print(f"del fruits[0]: {fruits}")
del fruits[1:3] 
print(f"del fruits[1:3]: {fruits}")

print("\n"+"="*40+"\n")
#clear 모든 요소 삭제
fruits.clear()
print(f"clear : {fruits}")

print("\n"+"="*40+"\n")


