#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/6 20:23
from flask import render_template

from app.web import web
from app.web.models import ProjectInfo


@web.route('/')
def index():
    # 数据层逻辑
    # all()
    projects = ProjectInfo.query.all()
    return render_template('index.html', projects=projects)