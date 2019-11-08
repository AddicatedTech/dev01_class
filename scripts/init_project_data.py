#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/8 20:
from app.web.models import ProjectInfo, db
from run import app


def add_project(nums):
    # 推入上下文
    with app.app_context() as ctx:
        for i in range(nums):
            project = ProjectInfo(project_name=f'project{i}', simple_desc=f'project{i},简介')
            db.session.add(project)
        db.session.commit()

def edit_project(project_id):
    with app.app_context() as ctx:
        project = ProjectInfo.query.get(project_id)
        project.project_name = '修改后的项目'
        db.session.add(project)
        db.session.commit()

if __name__ == '__main__':
    edit_project(3)