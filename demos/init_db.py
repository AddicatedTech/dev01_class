#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/6 21:13

# 引入app, db
from app import app, db

with app.app_context() as ctx:
    db.create_all()