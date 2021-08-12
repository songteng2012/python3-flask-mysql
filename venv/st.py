from flask import Flask
from flask import request
from st_conn import conn


app = Flask(__name__)
# 学生信息students
# R: Read   读取students /GET
# C: Create 创建students /POST
# U: Update 更新students /PUT
# D: Delete 删除students /DELETE
@app.route('/students', methods=['GET', 'POST','PUT','DELETE'])
def students():
    if request.method == 'GET':
        cursor = conn.cursor()
        try:
            query = "select * from students"
            cursor.execute(query)
            conn.commit()
            results = cursor.fetchall()
            print(results)
        except Exception as e:
            print(e)
        sno = request.args.get('sno',type=int,default=None)
        if sno == 1:
            return dict(sno='sno from get')
        else:
            return dict(sno='no exit')

    elif request.method == 'POST':
        # 1.获取游标
        cursor = conn.cursor()
        try:
            #2.写sql语句
            query = "insert into students (sno,sname,ssex,sbirthday,sclass) values('003','王丽','女','1976-01-23','三班')"
            # 3.执行sql
            cursor.execute(query)
            # 4.提交事务
            conn.commit()
            # 5.接受全部的返回结果行
            results = cursor.fetchall()
            print(results)
        # 6.抛出异常
        except Exception as e:
            print(e)
        #7.post接口返回值
        print(request.form)
        print(request.data)
        print(request.json)
        sno = request.json.get('sno')
        if sno == 2:
            return dict(sno='sno from post')
        else:
            return dict(sno='no exit')

    elif request.method == 'PUT':
        cursor = conn.cursor()
        try:
            query = "update students set sname='张三' where sno='3';"
            cursor.execute(query)
            conn.commit()
            results = cursor.fetchall()
            print(results)
        except Exception as e:
            print(e)
        sno = request.args.get('sno',type=int,default=None)
        if sno == 3:
            return dict(sno='sno from put')
        else:
            return dict(sno='no exit')

    elif request.method == 'DELETE':
        cursor = conn.cursor()
        try:
            query = "DELETE FROM students WHERE sno=3;"
            cursor.execute(query)
            conn.commit()
            results = cursor.fetchall()
            print(results)
        except Exception as e:
            print(e)
        sno = request.args.get('sno',type=int,default=None)
        if sno == 4:
            return dict(sno='sno from delete')
        else:
            return dict(sno='no exit')


