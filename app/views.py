from flask import current_app, render_template
from .models import *
from app import app

@app.route('/')
@app.route('/home')
def index():
	return render_template("index.html",title="Home",css="index")