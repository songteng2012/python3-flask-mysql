from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'GET':
        return dict(username='songteng',sex='male')
    else:
        return dict(username='yao',sex='female')



@app.route('/students_1', methods=['GET', 'POST','PUT','DELETE'])
def students_1():
    if request.method == 'GET':
        sno = request.args.get('sno','')
        if sno == '001':
            return dict(sno='sno from get')
        else:
            return dict(sno='sno from post')

    elif request.method == 'POST':
        print(request.form)
        print(request.data)
        print(request.json)
        sno = request.json.get('sno')
        if sno == '100':
            return dict(sno='100',sname='songteng5467',ssex='male',sbirthday='1988-10-06',sclass='一百班')
        else:
            return dict(sno='200',sname='yao986464',ssex='female',sbirthday='1992-04-08',sclass='二百班')