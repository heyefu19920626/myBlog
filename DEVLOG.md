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
- 创建管理员账户
> python manage.py createsuperuser
- 创建应用
> python manage.py startapp blog
- 安装应用,在setting.py中安装
> 'blog'
- 在blog/models.py中创建模型
``` python
class Category(models.Model):
    name = models.CharField(max_length=100)
```
- 在blog/admin.py中注册模型
``` python
from blog.models improt Category

admin.site.register(Category)
```
- 修改数据库
> python manage.py makemigrations blog  
> python manage.py migrate
- 修改myBlog/urls.py,引入blog应用的url
> path('', include('blog.urls'))
- 创建基础模板base.html和首页模板index.html
- 在blog/views.py中创建首页视图函数
``` python
def index(request):
    return render(request, 'blog/index.html')
```
- 新建blog/urls.py,并创建对应的首页连接
``` python
from django.urls import path
from . import views

urlpattern =[
    path('', views.index, name='index'),
]
```
- 收集静态文件
> python manage.py collectstatic
- 在blog/view.py中创建国际化函数chang_language
- 在blog/url.py中添加url,并注册应用名称
> app_name = 'blog'  
> path('change_language/<language>/', views.change_language, name='change_language')
- 在base.html中添加切换语言的功能
- 在bolg/view中修改index视图,给前台返回所有博文列表
- 修改blog/url.py与index.html使首页正常显示
- 添加article_details.html模板作为文章详情页
> {{ article.body | safe }}
- 添加article_details视图函数,给前台返回对应文章信息
- 添加文章详情的url
- 安装支持markdown语法和高亮的模块
> pip install markdown  
> pip install Pygments
- 引入相关css文件