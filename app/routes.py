from flask import render_template, request, url_for, redirect, flash, session
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import User, current
from flask_login import LoginManager, login_user, logout_user
# from app.index import win

'''When the program runs, if the user is logged in, 
the value of the login_manager variable will be the user model class record for the current user'''
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(curr_player):
    if current(curr_player) is not None:
        player = User.query.get(int(curr_player))
    return player

@app.route('/')  #home page
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])   #login page
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():   #determine whether the form was submitted and validate the form data
            session['username'] = request.form.get('username')
            session.permanent = True
            session['password'] = request.form.get('password')
            remember_me = request.form.get('remember_me', False)
            player = User.query.first()
            if session['username'] == player.username and player.validate_password(session['password']):   #compare the submitted data with the data in database
                login_user(player)
                flash('Login successfully!', 'message')
                return render_template('sobokan.html', title='Log in', player=player)   #go to game page
            else:
                flash('Incorrect username or password!', 'error')
                return redirect(url_for('login'))   #return to login page
        else:
            flash('Invalid Input!', 'error')
    return render_template('login.html', title='Log in', form=form)

@app.route('/register', methods=['Get','POST'])  #register page
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session['username'] = request.form.get('username')
        session['password'] = request.form.get('password')
        if not session['username'] or not session['password']:   #determines whether the user has entered data
            flash('Invalid input!')
        player = User(username=session['username'], password=session['password'], scores=0)  #Creating a new player
        db.session.add(player)
        db.session.commit()
        flash('New player is created.', 'message')
        return render_template('login.html', title='Log in', form=form)
    else:
        flash('Invalid Input!', 'error')
    return render_template('register.html', title='Register', form=form)

@app.route('/signout')   #sign out page
def logout():
    logout_user()
    flash('You were logged out. Goodbye!', 'message')
    return redirect(url_for('login'))   #return to signin page

@app.route('/sokoban', methods=['GET', 'POST'])   #game page
def sokoban():
    player = session.get('username')
#    player.scores = player.scores + int(scores)
    db.session.commit()
    return render_template('sokoban.html', title='Game')

@app.route('/view', methods=['GET', 'POST'])   #view data page
def view():
    player = session.get('username')  # Reading user records
    if not player:
        flash('Only logged-in accounts can view data.', 'warning')
        return redirect(url_for('sobokan'))
    return render_template('view.html', player=player)
