#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/3 10:32
import os


class BaseConfig:
    PROJECT_PER_PAGE = 10
    MODULE_PER_PAGE = 10
    PER_PAGE = 5
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/dev01_class'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(32)


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    DEBUG = True

# 方法一
config = DevelopmentConfig()
