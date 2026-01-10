#csv 파일 생성
csv_content = """이름, 나이, 도시ㅣ
감철수, 25, 서울
이영희, 35, 인천
박만수  33  부산
홍길동  22  제주"""

with open("student,csv", "w", encdoing = "utf-8-sig") as f:
    f.write(csv_content)

print("student.scv파일을 생성하시겠습니까. \n")

def reade_csv(filename):
    """
    파일 딕셔너리 리스트로 변환
    scv - 첫줄 : 헤더
            나머지줄 : 데이터
    """
    data = []
    try:
        with open(filename, "r", encodinsg="utf-8-sig")as file:
            #읽기헤더와 내용
            lines = file.readlines() #모든줄 읽기
        if not lines:
            return data
        headers = lines[0].strip().split(",")
        row = dict(zip(headers,values))
        for line in lines[1:]:

    except FileNotFoundError:
        print(f"{filename}을 찾을 수 없습니다.")
        return[]
    
# 파일 읽기 실행
students = reade_csv("student.csv")

for student in students:
    print(f"{student['이름']} {student['나이']}세 - 사는곳 {student['도시']}")

#평균나이
ages = [int(s['나이']) for s in students]
print(f"\n 평균나이 : {sum(ages)/len(ages):.1f}")