import json

print("========== 학생정보 관리 ==========")
students = []

while True:
    print("\n1. 학생추가")
    print("2. 전체 학생 보기")
    print("3. 저장 및 종료")

    choice = input("선택: ")

    if choice == '1':
        name = input("이름: ")
        age = int(input("나이: "))
        grade = input("학년: ")
        student = {
            'name':name,
            'age':age,
            'grade':grade
        }
        students.append(student)
        print("학생 정보가 새로 추가되었습니다.")

    elif choice == '2':
        for i, student in enumerate(students, 1):
            print(f"{i}. {student['name']}({student['age']}세,{student['grade']})")
    
    elif choice =='3':
        with open('students.json','w',encoding='utf-8') as f:
            json.dump(students, f, ensure_ascii=False, indent=4)
        print("저장 완료!")
        break