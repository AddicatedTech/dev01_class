#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/6 20:16
#MVC 分层思想
# wtf 验证层。

from flask import Blueprint

web = Blueprint('web', __name__)

# 路由
from .views import index, cases, modules, projects, suites

# 大型应用 路由==> app



