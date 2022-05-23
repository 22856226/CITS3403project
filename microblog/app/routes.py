from flask import render_template, flash, redirect,request,session
from flask import Flask, url_for
from app import app, db
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User,Post
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse
from app.forms import RegistrationForm

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        return render_template('sokoban.html')
    else:
        username= current_user.username
        level1 = request.form.get("scores1")
        level2 = request.form.get("scores2")
        level3 = request.form.get("scores3")
        id_num = current_user.id
        data = Post.query.filter_by( user_name = username).first()
        if data is None:
            datas = Post(level1=level1, level2 = level2 ,level3 = level3,user_id = id_num, user_name = username)
            db.session.add(datas)
            db.session.commit()
        else:
            data.level1 = level1
            data.level2 = level2
            data.level3 = level3
            db.session.commit()
    return render_template('sokoban.html')
@app.route('/play')
def play():
    return render_template('sokoban.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route('/user/<username>')

@app.route('/ranking')
def ranking():
    content = db.session.query(Post).all()
    return render_template('ranking.html',  content=content)

