from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['user']
    password = request.form['pwd']
    if username=='admin' and password=='password': #check whether the user is correct
        return render_template('signin_ok.html', username=username)
    if username==" ":
        return render_template('form.html', message='Please enter your username', username=username)
    if password==" ":
        return render_template('form.html', message='Please enter your password', username=username)
    return render_template('form.html', message='Incorrect username or password', username=username)

if __name__ == '__main__':
    app.run()
