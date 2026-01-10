# 반복 순환문 적용시
person = {
  "name":"김철수",
  "age":20,
  "major":"게임개발",
  "grade":3
}

for key in person:
  print(key)  #  value호출시  person[key]

print("\n"+"="*40+"\n")

for key in person.keys():
  print(key)

print("\n"+"="*40+"\n")

for value in person.values():
  print(value)

print("\n"+"="*40+"\n")

for key,value in person.items():
  print(f"{key}:{value}")