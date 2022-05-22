import hashlib
from os import uname
from flask import render_template, request
from  app import *
from module import *
#decorator
def login_requir(func):
    @wraps(func)
    def inner(*args,**kwargs):
        user=session.get('username') 
        if not user:
            return redirect('/login') 
        return func(*args,**kwargs)
    return inner


@app.route('/register',methods=["GET","POST"])
def add_user():
    if request.method=="GET":
        user_list=User.query.all()
        return render_template("register.html", user_list=user_list)
    else:
        username=request.form.get("username")
        password=hashlib.md5(request.form.get("password").encode()).hexdigest() 
        user_list=request.form.get("user_list")
        user=User(username=username,password=password)
        user.save()
        return redirect("/login")

@app.route('/home')
@login_requir
def detail_user():
    detail = User.query.all(id)
    order = User.query.order_by('-s_id').limit(10)
    return render_template("home.html",detail=detail , order= order)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        form = request.form
        username = form.get('email')
        password = form.get('password')
        session['username'] = username
        if username == username and password == password:
            return redirect(url_for('index'))
        else:
            error = 'erroe of uname or pwd'
            flash(error)
            return redirect(url_for('login'))
    else:
        return render_template("login.html", error=error)

@login_requir
@app.route("/?",methods=['GET','POST'])
def update():
    user = User.query.get(id)
    if request.method == "POST":
        results = request.form.get('moves_data')
        db.updatedata(results)
        db.session.commit()
        
        return render_template("?.html",results=results)