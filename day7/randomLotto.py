import random
#로또번호 생성기
print("===오늘의 로또번호 ===")
lotto = random.sample(range(1,46),6)
lotto.sort()
print("이번 주 행운의 로또 번호: ", lotto)

#점심 메뉴 추천기
menus = ['불고기','짜장면','돈까스','짬뽕','파스타','피자','초밥']
recommend = random.choice(menus)
print(f"=== 오늘의 추천메뉴: {recommend}")

#주사위 게임
print("컴퓨터와 주사위 대결 게임")
input("Enter를 눌러보세요.")
player = random.randint(1,6)
computer = random.randint(1,6)

if player > computer:
    print("유저 승리!")
elif player < computer:
    print("컴퓨터 승리!")
else:
    print("무승부!")

#팀 무작위 배정
members = ['철수', '영희','길동','민수','지영','동현','수진']
random.shuffle(members)
team1 = members[:3]
team2 = members[3:]


#확률적 이벤트(크리티컬 히트 -- 게임)
if random.random() < 0.3:
    print("크리티컬 히트!")