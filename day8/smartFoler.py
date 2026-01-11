#프로젝트 구조 자동 생성기
import os
from datetime import datetime

class FolerManager:
    """폴더 관리"""
    def create_project_structure(self, project_name):
        """프로젝트 폴더 구조 자동 생성"""
        if os.path.exists(project_name):
            print(f"{project_name} 폴더가 이미 있습니다.")
            return
        folders=[
            project_name,
            f"{project_name}/src",
            f"{project_name}/data",
            f"{project_name}/docs",
            f"{project_name}/images"
        ]
        for folder in folders:
            os.makedirs(folder,exist_ok=True) # 폴더가 이미 존재 해도 에러 발생되지 않음
            print(f"{folder} 생성")

        # README 파일 생성
        readme_path = os.path.join(project_name, 'README.md')
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {project_name} \n\n")
            f.write(f"생성일 : {datetime.now().strftime('%Y-%m-%d')}\n")
        print(f"'{project_name}'프로젝트 생성 완료!")

manager = FolerManager()
manager.create_project_structure("MyPythonApp")