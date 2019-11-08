"""web 服务器运行。
选用 gunicorn, uwsgi, waitress。


一切皆为对象，

"""

from app import create_app

app = create_app()

# 导入数据，migate flask db init
# db 推入上下文，db.create_all()

if __name__ == '__main__':
    print(app.config['DEBUG'])
    app.run(port=5002)

