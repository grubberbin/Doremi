# Doremi

- 全国知名幼儿教育机构哆唻咪启蒙乐园官网
- 去掉上面的知名

### 环境
- Python 3.7
- Django 2.2.3
- xadmin 2.0.1
- Pycharm


### 网站功能




### 快速部署
- 代码拉取  

    `git clone git@github.com:grubberbin/Doremi.git`  
    
- 三方包导入 
     
    注意 xadmin  导入   
    `pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2`
    
- 数据库迁移  
    
    为方便项目演示，可先将settings.py中的数据库配置使用splite3
    ```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'Doremi',
        # 'USER': 'root',
        # 'PASSWORD': '12345678',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        }
    }
    ```
    然后依次运行   
    `makemigrations`  
    `migrate`    
    `ceatesuperuser`  
    
- 运行  

    `python manage.py runserver 0.0.0.0:8000`



###关于项目
   
   - 前端代码是从网上下载，修改成Django使用的模板，前端渣渣。  
   - 整体的项目架构参考 [高仿慕课网：py3.5 + Django1.10 + xadmin 搭建的在线课程教育平台](https://github.com/zaxlct/imooc-django)  表示感谢！
   - 虚心接受各位大神的批评指正，感谢！
   - 如果对你有帮助那你就点个小星星吧