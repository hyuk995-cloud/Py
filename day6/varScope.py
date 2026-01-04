global_var = "전역변수"
def tmp_function():
    local_var = "지역변수"
    print(f"전역변수 : {global_var}")
    print(f"지역변수 : {local_var}")

tmp_function()

print(f"전역변수 : {global_var}")
# print(f"지역변수 : {local_var}") 인식할 수 없음

x = 10
def test1():
    x = 20
    print(f" inside x : {x}") # 20나옴
test1()

print(f"outside x : {x}") # 10나옴
#global keyword
count = 0
def increment():
    global count # 전역변수 사용의미 --- 가급적 사용 자제
    print(f"count: {count}")

increment()    
increment()    
increment()
print(F"final count: {count}")

countNum = 0
def increment2(n): #global 대신 권장 방법 - 매개변수, return활용
    return n+1

countNum = increment2(countNum)
countNum = increment2(countNum)
countNum = increment2(countNum)
print(f"final countNum: {countNum}")