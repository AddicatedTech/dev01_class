#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/6 21:27

from flask import render_template

from app.web import web


@web.route('/list_cases')
def list_cases():
    return 'projects'

@web.route('/create_case')
def create_case():
    return 'projects'