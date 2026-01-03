#대화 목록
friends = {"철수", "영희", "만수", "철수", "지혜"}
print(f"친구들 : {friends}")

#빈세트 생성
empty_set = set()
empty_dict = {}
print(f"set() 타입: {type(empty_set)}")
print(f"{{}} 타입: {type(empty_dict)}")

#리스트를 세트로
numbers_list = [1,2,2,3,3,3,4,5,5]
numbers_sete = set(numbers_list)
print(f"리스트 : {numbers_list}")
print(f"세트 : {numbers_sete}")

#문자열 세트로
text = "hello"
char_set = set(text)
print(f"문자 세트 : {char_set}")

#-----------------------------------------------------

numbers = {1, 2, 3, 4, 5}
#길이
print(f"길이 : len({numbers}) = {len(numbers)}")

#포함여부(매우 빠름)
print(f"\n3 in {numbers}: {3 in numbers}")
print(f"\n10 in {numbers}: {10 in numbers}")
print("\n"+"="*30+"\n")

#최대 최소 합계
print(f"최대값: {max(numbers)}")
print(f"최소값: {min(numbers)}")
print(f"합계 : {sum(numbers)}")
print("\n"+"="*30+"\n")

#set 비교(※순서 무관)
set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {3, 2, 1}
set4 = {1, 2, 4}
print(f"seti == set2 : {set1==set2}") #true
print(f"seti == set3 : {set1==set3}") #true
print(f"seti == set4 : {set1==set4}") #false
print("\n"+"="*30+"\n")

original = {1,3,6}
copy1 = original.copy()
copy2 = set(original)

copy1.add(4)
original.add(7) # 오리지날에 7추가 -> 영향 없음
print(f"원본 : {original}")
print(f"복사1 : {copy1}")
print(f"복사2 : {copy2}")

#요소 삭제
fruits = {"사과", "바나나", " 복숭아"}
fruits.remove("바나나")
print(f"바나나 삭제 :{fruits}")
#fruits.remove("키위") 없는 값 삭제 요청시 에러 발생
fruits.discard("키위") #문제 없음
fruits.update({"멜론","수박","딸기"})
print(f"업뎃 : {fruits}")

#임의 요소 삭제
removed = fruits.pop()
print(f"pop반환 요소 {removed}")
print(f"pop()결과 : {fruits}")
#=====================================================

group_a = {"민준", "서연", "지우", "하준"}
group_b = {"서연", "도윤", "예준", "지우"}
print(f"그룹 A:{group_a}")
print(f"그룹 B:{group_b}")
group_a.add("은우")

#합집합
uinon_set = group_a.union(group_b)
print(f"합집합 : {uinon_set}")

#교집합
intersection_set = group_a.intersection(group_b)
print(f"교집합 : {intersection_set}")

#차집합 // a - b = a에서 b를 빼고 남은 a들만 출력
difference_set = group_a.difference(group_b)
print(f"차집합 (A-B) : {difference_set}")

#대칭 차집합 // a- b = a에서 b를 뺴고 남은 a들이랑, b - a를 해서 b에서 a를 뺴고 남은 애들을 합친 값 출력
symmentric_difference_set = group_a.symmetric_difference(group_b)
print(f"대칭차집합 : {symmentric_difference_set}")

#========================================
print("\n"+"="*30+"\n")
#========================================

kim_hobbies = {"독서", "영화", "운동", "음악"}
lee_hobbies = {"게임", "영화", "음악", "요리"}

kim_lee_hobbies = kim_hobbies.intersection(lee_hobbies) 
#kim_hobbies & lee_hobbies로 입력하면 간단하게 가능
print(f"공통관심사 : {kim_lee_hobbies}")

kim_odd_lee = kim_hobbies.difference(lee_hobbies) 
# kim_hobbies - lee_hobbies로 입력하면 간단하게 가능
print(f"kim만의 관심사 : {kim_odd_lee}")

kim_lee_symmentric = kim_hobbies.symmetric_difference(lee_hobbies) 
# kim_hobbies ^ lee_hobbies 로 입력하면 간단하게 가능
print(f"kim과 lee의 중복된걸 뺀 고유 관심사 : {kim_lee_symmentric}")
