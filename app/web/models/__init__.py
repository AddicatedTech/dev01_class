#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/6 20:44
import time

from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    # 数据的生成时间
    created_at = db.Column(db.Integer, default=int(time.time()))
    # 数据的修改
    updated_at = db.Column(db.Integer, default=int(time.time()), onupdate=int(time.time()))
    # status
    status = db.Column(db.SmallInteger, default=1)

    @classmethod
    def all(cls):
        return cls.query.order_by(desc(cls.updated_at)).all()

    @classmethod
    def paginate(cls, page):
        """分页器"""
        return cls.query.paginate(
            page=int(page), per_page=current_app.config['PER_PAGE'], error_out=False)


class User(Base):
    username = db.Column(db.String(32), nullable=False, default='', unique=True)


class ProjectInfo(Base):
    project_name = db.Column(db.String(32), nullable=False, default='', unique=True)
    simple_desc = db.Column(db.String(500), nullable=False, default='')









