#짝수 판단
is_event = lambda x: x%2 == 0
print(f"10은 짝수야? {is_event(10)}")

print("\n"+"="*40+"\n")#=====================================================

#즉시실행
result = (lambda a, b: a*b)(5,3) #lambda함수 정의 후 바로 실행
result = lambda a, b: a*b

print("\n"+"="*40+"\n")#=====================================================

#조건부 표현식
get_max = lambda a, b: a if a>b else b # 값1 if 조건 else 값2( if 조건이 참일때 값1이고, 아니면 값2)
print(f"max(10,20): {get_max(10,20)}")

def square(x):
    return x**2

numbers=[1, 2, 3, 4, 5]
squarde = list (map(square, numbers))
print(f"원본 : {numbers}")
print(f"제곱 : {squarde}")

numbers2 = [1,2,3,4,5]
squarde2 = list(map(lambda x:x**2, numbers2))
print(f"람다 제곱: {squarde2}")

print("\n"+"="*40+"\n")#=====================================================

#대문자 변환
names = ["alpha","bravo","charlie"]
upper_names = list(map(lambda x:x.upper(), names))
print(f"대문자 이름: {upper_names}")
print("\n"+"="*40+"\n")#=====================================================

#세금 10%포함 가격 계산
price = [1000,2000,3000]
with_tax = list(map(lambda a:int(a*1.1), price))
print(f"세금포함(정수)가격 : {with_tax}")
print("\n"+"="*40+"\n")#=====================================================

#멀티 시퀀스
nums1 = [1,2,3]
nums2 = [10,20,30]
sums = list(map(lambda x, y: x+y, nums1, nums2))
print(f"합계: {sums}")
print("\n"+"="*40+"\n")#=====================================================

#filter()함수 -- 요소 걸러내기
number = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda a:a%2==0, number))
print(f"number중 짝수: {evens}")

print("\n"+"="*40+"\n")#=====================================================

#제품 가격 필터링
products = [
    {"name":"노트북","price":1800000},
    {"name":"마우스","price":35000},
    {"name":"키보드","price":85000},
    {"name":"모니터","price":450000}
]

#10만원 이상은 고가 제품
expensive = list(filter(lambda x:x["price"]>=100000, products))
print("\n=== 고가 제품 ===")
for p in expensive:
    print(f"{p['name']}: {p['price']:,}원")

# 응용 key 매개 변수로 요소 비교 결정
by_price = sorted(products, key=lambda x:x["price"])
print("\n===가격 순 ===")
for p in by_price:
    print(f"{p['name']}: {p['price']:,}원")

#조건부 표현식
get_grade = lambda score:"A" if score >=90 else "B" if score>=80 else "F"
print(f"95점: {get_grade(95)}")
print(f"95점: {get_grade(82)}")
print(f"95점: {get_grade(77)}")

print("\n"+"="*40+"\n")#=====================================================

#여러값 반환(튜플)
process = lambda x: (x*2, x**2, x+10)
result = process(5)
print(f"5를 process처리 : {result}")


#딕셔너리 람다
operations = {
    "add" : lambda a, b:a+b,
    "sub" : lambda a, b:a-b,
    "mul" : lambda a, b:a*b,
    "div" : lambda a, b: a/b if b != 0 else "Error"
}
print(f"10+5 = {operations['add'](10,5)}")
print(f"10-5 = {operations['sub'](10,5)}")
print(f"10X5 = {operations['mul'](10,5)}")
print(f"10/5 = {operations['div'](10,5)}")