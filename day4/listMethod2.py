# 리스트 정렬
# sort() -- 오름차순 정렬
numbers = [3,1,8,7,2,5,4,6,9]
numbers.sort()
print(f" 오름차순 정렬: {numbers}")
# 내림차순 정렬
numbers.sort(reverse=True)
print(f" 내림차순 정렬: {numbers}")

print("\n"+"="*40+"\n")
#sorted() -- 정렬된 새 리스트 반환, 원본 유지
nums = [3,1,8,7,2,5,4,6,9]
sorted_nums = sorted(nums)

print(f"원본 배열 : {nums}")
print(f"sorted 배열 : {sorted_nums}")
print("\n"+"="*40+"\n")
# [ 알파벳 순서, 대문자 우선 ] , 대소문자무시(  .sort(key=str.lower)  )
alphabet = ["Bravo", "Charlie", "delta", "alpha"]
alphabet.sort()
print(f"기본정렬 : 대문자우선:{ alphabet }")
alphabet.sort(key=str.lower)
print(f"기본정렬 : 대문자무시:{ alphabet }")
#revers() 순서 뒤집기
alphabet.reverse()  # alphabet[::-1] 반환
print(f"역순 정렬 :{ alphabet }")
