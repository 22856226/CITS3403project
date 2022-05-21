from flask import render_template, request, url_for, redirect, flash
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import User
from flask_login import LoginManager, login_user, login_required, logout_user

'''When the program runs, if the user is logged in, 
the value of the login_manager variable will be the user model class record for the current user'''
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    player = User.query.get(int(user_id))
    return player

@app.route('/')  #home page
def home():
    return render_template('home.html')

@app.route('/intro')  #introduction page
def intro():
    return render_template('intro.html')

@app.route('/login', methods=['GET', 'POST'])   #login page
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():   #determine whether the form was submitted and validate the form data
            username = request.form.get('username')
            password = request.form.get('password')
            remember_me = request.form.get('remember_me', False)
            player = User.query.first()
            if username == player.username and player.validate_password(password):   #compare the submitted data with the data in database
                login_user(player)
                flash('Login successfully!')
                return redirect(url_for('intro'))   #return to login page
            else:
                flash('Incorrect username or password!')
                return redirect(url_for('login'))   #return to login page
        else:
            flash('Invalid Input!')
    return render_template('login.html', title='Log in', form=form)

@app.route('/register', methods=['GET', 'POST'])  #register page
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            if not username or not password:   #determines whether the user has entered data
                flash('Invalid input!')
            player = User(username=username, password=password)  #Creating a new player
            db.session.add(player)
            db.session.commit()
            return render_template('login.html', title='Log in', form=form)
            flash('New player is created.')
        else:
            flash('Invalid Input!')
    return render_template('register.html', title='Register', form=form)

@app.route('/signout')   #sign out page
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('login'))   #return to signin page
