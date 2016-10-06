# my_blog
flask_blog
1.用户登录 使用 Werkzeug实现密码散列 ，通过保存散列码来认证用户输入的密码
2.用户注册 使用itsdangerous生成确认令牌 ，用户在邮箱中打开带有令牌的网址 才能确认登录
3.用户头像 通过计算电子邮件地址的 MD5 散列值 ，在Gravatar获取头像图片
4.博客文章 使用 Markdown和Flask-PageDown支持的富文本文章
5.虚拟信息 用ForgeryPy包生成虚拟用户和数据
6.博客使用了用Flask-SQLAlchemy sqlite来保存数据
7.表单 均使用了 WTF提供模板 ，界面 Flask-Bootstrap集成Twitter Bootstrap
