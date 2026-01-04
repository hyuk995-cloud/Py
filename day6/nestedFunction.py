#중첩 함수
def outer():
    outer_var = "외부함수내 변수"
    
    def inner():
        inner_var = "내부 함수 내 변수"
        print(f"내부 함수 :")
        print(f"외부 변수: {outer_var}")
        print(f"내부 변수 : {inner_var}")
    
    inner()
    print(f"\n외부 함수")
    print(f"외부 변수 : {outer_var}")
    # print(f" 내부 변수:{inner_var}")#에러 = 내부 함수 내 변수 접근 불가
outer()

print("\n"+"="*40+"\n")#=====================================================

#nonlocal keyword

def outer2():
    count = 0
    def increment():
        nonlocal count #외부 함수에 있는 카운트 정의
        count += 1
        return count
    print(increment())
    print(increment())
    print(increment())

outer2()

print("\n"+"="*40+"\n")#=====================================================

#Clousure -- 클로저 : 함수를 반환, 반환된 함수는 외부함수 변수를 기억(기록)
def make_multopl(n):
    def multiplier(x):
        return x*n
    return multiplier

times2 = make_multopl(2) # n=2인 multiplier함수
times3 = make_multopl(3)
print(f"\n 5x2 = {times2(5)}") # make_multopl(2)(5)
print(f"\n 5x3 = {times2(5)}")
print(f"\n 5x10 = {times2(10)}")
