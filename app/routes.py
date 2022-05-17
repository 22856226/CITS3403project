from flask import render_template, request, url_for, redirect, flash
from app import app
from app.forms import LoginForm, RegisterForm
from app.store_pwd import User, db
from flask_login import LoginManager, login_user, login_required, logout_user

'''When the program runs, if the user is logged in, 
the value of the login_manager variable will be the user model class record for the current user'''
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    player = User.query.get(int(user_id))
    return player

@app.route('/login', methods=['GET', 'POST'])   #login page
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            remember_me = request.form.get('remember_me', False)
            player = User.query.first()
            if username == player.username and player.validate_password(password):
                login_user(player)
                flash('Login successfully!')
                return redirect(url_for('login'))   #return to login page
            else:
                flash('Incorrect username or password!')
                return redirect(url_for('login'))   #return to login page
        else:
            flash('Invalid Input!')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST']).  #register page
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            if not username or not password:
                flash('Invalid input!')
            player = User(username=username, password=password)
            db.session.add(player)
            db.session.commit()
            flash('New player is created.')
        else:
            flash('Invalid Input!')
    return render_template('login.html', form=form)

@app.route('/signout')   #sign out page
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('login'))   #return to signin page
