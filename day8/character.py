import json

character = {
    'name':'기사',
    'level':15,
    'hp':770,
    'item':['검','방패','물약']
}

with open('game_save.json','w',encoding='utf-8') as f:
    json.dump(character, f, ensure_ascii=False, indent=4)
print('게임 저장 완료')

#게임 불러오기

with open('game_save.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f) # 객체로 데이터 로드

print(f"\n 게임 데이터 로드 완료")
print(f"이름: {loaded_data['name']}")
print(f"레벨: {loaded_data['level']}")