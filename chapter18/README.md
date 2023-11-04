### django框架

```shell
# Django新建一个名为learning_log的项目。这个命令末尾的句点让新项目使用合适的目录结构，这样开发完成后可轻松地将应用程序部署到服务器。
# 千万别忘了这个句点，否则部署应用程序时将遭遇一些配置问题。如果忘记了这个句点，要删除已创建的文件和文件夹（ll_env除外），再重新运行这个命令
django-admin startproject learning_log .
ls
# Django新建了一个名为learning_log的目录，还创建了文件manage.py。后者是一个简单的程序，接受命令并将其交给Django的相关部分运行。我们将使用这些命令来管理使用数据库和运行服务器等任务。
# learning_log ll_env manage.py
ls learning_log
# 文件settings.py指定Django如何与系统交互以及如何管理项目。在开发项目的过程中，我们将修改其中一些设置，并添加一些设置。文件urls.py告诉Django，应创建哪些页面来响应浏览器请求。文件wsgi.py帮助Django提供它创建的文件，这个文件名是Web服务器网关接口（Web server gateway interface）的首字母缩写。
#  __init__.py settings.py urls.py wsgi.py
# 创建sqlite3
python manage.py migrate
# 启动服务，默认只能本地访问，修改settings.py文件，将默认值[]，改为['*']，允许所有IP访问
ALLOWED_HOSTS = ['*']
python manage.py runserver
```

```shell
# Django搭建创建应用程序所需的基础设施
python manage.py startapp appname
# 会在当前目录下新增appname的文件夹
cd appname
ls
# __init__.py admin.py    apps.py     migrations  models.py   tests.py    views.py
# models.py来定义要在应用程序中管理的数据
# 

```
