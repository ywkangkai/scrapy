
from flask import Flask,render_template,request,jsonify,abort


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('xialuo01.html')
    else:
        data = request.json
        if not data:
            abort('403')
        username = data.get('mobile')
        password = data.get('pwd')
        print(username,password)
        return jsonify({'success':'200'})

from base64 import b64encode
@app.route('/api',methods=['GET','POST'])
def indexs():
    if request.method == 'GET':
        a = '路漫漫其修远兮'
        b = '吾将上下而求索'
        data = {
            'data': [a,b]
        }
        return jsonify({'data':data})

if __name__ == '__main__':
    app.run()