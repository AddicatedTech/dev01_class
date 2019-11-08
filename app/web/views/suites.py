#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/1 17:21

from app.web import web


@web.route('/suites')
def suites():
    return 'suites'


@web.route('/get_suite/<int:s_id>')
def get_suite(s_id=None):
    return f'get project {s_id}'


@web.route('/edit_suite/<int:s_id>')
def edit_suite(s_id=None):
    return f'get project {s_id}'


@web.route('/create_suite')
def create_suite():
    return f'create project'


@web.route('/delete_suite/<int:s_id>')
def delete_suite(s_id=None):
    return f'delete project {s_id}'