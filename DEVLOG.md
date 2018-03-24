### 开发日志
----
- 安装虚拟环境
> python -m venv venv
- 激活虚拟环境
> source venv/bin/activate
- 安装django
> pip install django
- 在django中创建项目
> django-admin startproject myBlog .
- 创建数据库
> python manage.py migrate
- 修改myBlog/setting.py,增加国际化和静态文件支持
``` python
# 增加中间件支持
'django.middleware.locale.LocaleMiddleware',
# 增加i8n模块支持
'django.template.context_processors.i18n',
# 添加语言选项
LANGUAGES = [
    ("en-us", ("English")),
    ("zh-Hans", ("简体中文")),
]
# 添加本地化文件夹
LOCALE_PATH = (
    os.path.join(BASE_DIR, "locale"),
    )
# 设置静态文件根路径
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# 设置静态文件集合路径
STATICFILES_DIR = [
    os.path.join(BASE_DIR, "static"),
]
```
- 生成本地化文件
> python manage.py makemessages -l zh_Hans  
> python manage.py makemessages -l en
- 翻译之后编译本地文件
> python manage.py compilemessages

