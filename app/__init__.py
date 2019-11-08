"""初始化 app 核心对象.

配置相关的一些插件。
"""

from flask import Flask
from flask_migrate import Migrate

from app.config import config
from app.web.models import db
from app.web.template_env import str_time

app = Flask(__name__)
migrate = Migrate()

# app.config = Config()
#
# 其他的初始化东西，数据库

def create_app():
    """初始化"""
    # 初始化数据库
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    # 配置文件
    # 自定义的错误处理机制
    # 模板过滤器注册
    # app.add_template_filter

    # 注册蓝图
    from app.web import web
    app.register_blueprint(web)

    # 添加过滤器
    app.add_template_filter(str_time)

    return app
