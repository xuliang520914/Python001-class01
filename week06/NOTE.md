## 学习笔记

### MVC和MTV
- MVC是设计模式，是一种根据经验沉淀的编程的设计指导思想
- MTV是一种框架结构
  - M：模型
    - 创建模型
    - 执行CURD
  - T：模板
    - 页面结构
  - V：视图
    - 接收请求
    - 调用models
    - 调用templates
    - 将数据填充到模板再响应

### Django
  - 特点
    - 采用MTV的框架
    - 强调快速开发和代码复用
    - 组件丰富
      - ORM，即采用类的方式处理SQL关系与数据操作
      - URL支持正则
      - 模板可继承
      - 内置用户认证
      - admin管理系统
      - 内置表单模型、Cache缓存系统、国际化支持等等
  - 创建与目录简介
    - 安装`pip install django`
    - 创建项目`django-admin startproject 项目名称`
    - 在项目下的`manage.py`是命令行工具
    - 在项目下的项目名称目录下有一个`settings.py`是项目配置文件
      - 比如配置数据库信息、支持的应用程序等等

  - 应用程序
    - 创建应用程序
      - `python manage.py startapp 应用名称`
      - 对应的应用程序下有如下文件
        - migrations：数据库迁移文件
        - models.py：模型
        - apps.py：当前app的配置文件
        - admin.py：管理后台
        - test.py：自动化测试
        - views.py：视图
    - 启动应用
      - `python manage.py runserver 0.0.0.0:80`：可以指定端口
  - 配置文件包括如下
    - 项目路径
    - 密钥
    - 域名访问权限
    - App列表
    - 静态资源：CSS、JavaScript、图片等
    - 模板文件
    - 数据库配置
    - 缓存
    - 中间件
  - URL支持变量