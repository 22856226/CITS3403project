from flask import Flask, make_response, request, session, render_template, redirect

app = Flask(__name__)

@app.route('/login')

def login():
