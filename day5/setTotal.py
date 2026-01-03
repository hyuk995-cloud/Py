#학생관리 시스템
print("========== 종합 학생관리 시스템 =============")

students = [
    {
        "id" : "2026001",
        "name" : "김철수",
        "courses" : {"파이썬", "자료구조", "알고리즘"},
        "grades" : {"파이썬" : "A", "자료구조" : "B+"},
        "contact" : ("010-1111-2222","kim@gmail.com")
    },
    {
        "id" : "2026002",
        "name" : "이영희",
        "courses" : {"파이썬", "데이터베이스", "웹프로그래밍"},
        "grades" : {"파이썬" : "A", "데이터베이스" : "A"},
        "contact" : ("010-4444-6666","lee@gmail.com")
    },
    {
        "id" : "2026003",
        "name" : "박만수",
        "courses" : {"자료구조", "알고리즘", "운영체제"},
        "grades" : {"자료구조" : "B", "알고리즘" : "A"},
        "contact" : ("010-7777-3333","park@gmail.com")
    }
]

#전체학생정보
print(f"[ 전체학생정보 ]")
for student in students:
    print(f"\n학번: {student['id']}")
    print(f"이름 :{student['name']}")
    print(f"수강과목 :{', '.join(student['courses'])}")
    print(f"연락처 :{student['contact'][0]}")
#공통수강과목 찾기
all_courses = [s['courses'] for s in students] #리스트 컴프리헨션으로 모든 학생 coureses(set)을 리스트로 
# common_courses = all_courses[0] & all_courses[1] & all_courses[2] 도 가능하다
common_courses = set.intersection(*all_courses) #리스트 개별 인자 / 모든 set의 교집합 구하기
print(f"\n[공통 수강 과목]")
if common_courses:
    print(f"{', '.join(common_courses)}")
else:
    print("없음")
#전체개설 과목
all_unique_courses = set()
for student in students:
    all_unique_courses.update(student['courses'])

print(f"전채 개설 과목 ({len(all_unique_courses)})개")
for course in all_unique_courses:
    print(f"-{course}")

#과목별 수강생
print(f"\n[과목별 수강생]")
course_students = {} #과목명이 키(key), 수강생 이름 리스트를 값(value)으로 하는 비어있는 딕셔너리
for student in students:
    for course in student['courses']: #각 학생의 수강과목 순환
        if course not in course_students:
            course_students[course] = []
        course_students[course].append(student['name'])

# print(f"course_students : {course_students}")
for course in sorted(course_students.keys()): #과목명을 가나다 순으로 정렬, 반복 순환
    student_list= ', '.join(course_students[course])
    count = len(course_students[course])
    print(f"{course}({count}명) : {student_list}")

#성적 통계
print(f"\n[성적 통계]")
grade_points={"A+":4.5, "A":4.0, "B+":3.5, "B":3.0}
for student in students:
    total_points = 0
    count = 0
    for grade in student['grades'].values(): #values == a, b, a+ b+을 말함
        if grade in grade_points:
            total_points += grade_points[grade]
            count += 1
    if count>0 :
        gpa = total_points/count
        print(f"{student['name']}: 평점 {gpa:.2f}")


