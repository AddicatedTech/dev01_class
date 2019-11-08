#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/8 21:59
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class ProjectAddForm(FlaskForm):
    # form_model = ProjectInfo
    project_name = StringField(label='项目名称', validators=[DataRequired(), Length(
        max=64, min=1)])
    simple_desc = TextAreaField(label='项目描述', validators=[Length(max=512, min=0)])