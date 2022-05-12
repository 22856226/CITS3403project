from flask import render_template
from app import app
from app.forms import LoginForm



@app.route('/')
def login():
    form = LoginForm()
    return render_template('form.html',  form=form)
