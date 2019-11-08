#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/6 21:27

from flask import render_template

from app.web import web


@web.route('/list_modules')
def list_modules():
    return 'projects'

@web.route('/create_module')
def create_module():
    return 'projects'