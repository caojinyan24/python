
1. 创建项目
2. 创建应用:python manage.py startapp polls
3. 合并模块:python manage.py migrate
4. model发生改变时,告诉django对migrate做出修改:python manage.py makemigrations polls

数据库操作
1. 进入脚本环境:python manage.py shell

测试:
1. 运行单测:python manage.py test polls


遇到的问题:
页面报错:dictionary update sequence element #0 has length 1; 2 is required
错误原因:`{% url 'polls:detail' question.id %}`这里的`polls:detail`写成了`polls.detail`,使得取了polls的一个变量而报错,这里区分下变量和命名空间
