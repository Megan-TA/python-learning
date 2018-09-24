from flask import Flask, render_template, request, redirect, url_for, abort, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello flask'

@app.route('/index')
def index():
    print(request)
    return 'index'

# url传参
@app.route('/index/<name>')
def test_path(name):
    return name

# 模板渲染
@app.route('/form')
def form():
    return render_template('form.html')

# post类型请求
@app.route('/login', methods = ['GET', 'POST'])
def login():
    uname = request.form['name']
    upassword = request.form['password']
    return 'Post类型传递的参数是：' + '姓名：' + uname + '， 密码：' + upassword

# get类型请求
@app.route('/testGet')
def test_get():
    uname = request.args['name']
    return 'get类型传递的参数：' + uname

# 重定向
@app.route('/noPage')
def noPage():
    return redirect(url_for('form'))

# 错误提示（默认空页面）
@app.route('/error')
def error():
    abort(503)

# 自定义错误页面
@app.errorhandler(404)
def errorpage():
    return render_template('404.html'), 404

#更改响应内容信息
@app.route('/set')
def sets():
    response = make_response('自定义相应信息')
    response.headers['X-Something'] = 'A value'
    return response

if __name__ == '__main__':
    app.run(debug=1)