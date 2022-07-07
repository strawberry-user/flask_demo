from flask import Flask
from flask import request, render_template, redirect, url_for, escape


app = Flask(__name__)

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', name=name, movies=movies)


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/hello')
def hellp():
    return render_template('index.html', name='hansijie')


@app.route('/form', methods=['POST', 'GET'])
def bio_data_form():
    if request.method == "POST":
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        hobbies = request.form['hobbies']
        return redirect(url_for('showbio',
                                username=username,
                                age=age,
                                email=email,
                                hobbies=hobbies))
    return render_template("bio_form.html")


@app.route('/showbio', methods=['GET'])
def showbio():
    username = request.args.get('username')
    age = request.args.get('age')
    email = request.args.get('email')
    hobbies = request.args.get('hobbies')
    return render_template("show_bio.html",
                           username=username,
                           age=age,
                           email=email,
                           hobbies=hobbies)


if __name__ == '__main__':
    app.run(debug=True, port=5000)