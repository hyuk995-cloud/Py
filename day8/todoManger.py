import json
import os
from datetime import datetime

class TodoManager:
    def __init__(self):
        self.filename = "todos.json"
        self.todos = self.load_todos()
    
    def load_todos(self):
        """할일 불러오기"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8")as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """할일 저장하기"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=4)
        print("저장 완료")

    def add_todos(self, task):
        """ 할 일 추가"""
        todo = {
            "id":len(self.todos)+1,
            "task":task,
            "done":False,
            "created":datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"{task} 추가됨!")

    def show_todos(self):
        """할 일 목록 보기"""
        if not self.todos:
            print("할 일이 없습니다.")
            return
        print("\n 할 일 목록 :")
        for todo in self.todos:
            status = "★" if todo["done"] else "☆"
            print(f"[{status}]{todo['id']}, {todo['task']}")
    
    def complete_todo(self, todo_id):
        """할 일 완료 처리"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["done"] = True
                self.save_todos()
                print(f"'{todo['task']}' 완료!!")
                return
        print("해당 번호를 찾을 수 없습니다.")

manager = TodoManager()
manager.add_todos("파이썬 공부하기")
manager.add_todos("파이썬 복습하기")
manager.add_todos("운동하기")

manager.show_todos()
manager.complete_todo(1)

manager.show_todos()