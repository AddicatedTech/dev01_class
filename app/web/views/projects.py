#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/6 21:26

from flask import render_template, request

from app.web import web
from app.web.forms import ProjectAddForm
from app.web.models import ProjectInfo


@web.route('/list_projects')
def list_projects():
    # 自己生成假数据 faker
    page = request.args.get('page', 1)
    paginate = ProjectInfo.paginate(page)
    projects = paginate.items
    return render_template('projects.html', projects=projects, paginate=paginate)
# 分页
# 展示的不完全数据
# 注册过滤器，分离

@web.route('/create_project', methods=['GET', 'POST'])
def create_project():
    # 验证层
    form = ProjectAddForm()
    if request.method == 'GET':
        return render_template('project.html', form=form)
    return 'edit project'

@web.route('/edit_project/<int:p_id>')
def edit_project(p_id):
    return 'edit projects'

@web.route('/delete_project')
def delete_project():
    return 'delete projects'

# 编辑项目
# 不仅要展示，get, post
# 数据校验

# 删除项目
# 逻辑删除