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
                return render_template('sobokan.html', title='Log in', player=player)   #go to game page
            else:
                flash('Incorrect username or password!')
                return redirect(url_for('login'))   #return to login page
        else:
            flash('Invalid Input!')
    return render_template('login.html', title='Log in', form=form)

@app.route('/register', methods=['POST'])  #register page
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:   #determines whether the user has entered data
            flash('Invalid input!')
        player = User(username=username, password=password)  #Creating a new player
        db.session.add(player)
        db.session.commit()
        flash('New player is created.')
        return render_template('login.html', title='Log in', form=form)
    else:
        flash('Invalid Input!')
    return render_template('register.html', title='Register', form=form)

@app.route('/signout')   #sign out page
def logout():
    logout_user()
    flash('You were logged out. Goodbye!')
    return redirect(url_for('login'))   #return to signin page

@app.route('/sokoban', methods=['GET', 'POST'])   #game page
def sokoban():
 #   player.scores = player.scores + int(scores)
    return render_template('sokoban.html', title='Game')

@app.route('/view', methods=['GET', 'POST'])   #view data page
def view():
    players = User.query.all()  # Reading user records
    return render_template('view.html', players=players)
