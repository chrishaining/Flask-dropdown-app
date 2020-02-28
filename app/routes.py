from app import app, db
# from app.models import Player 
from flask import render_template, redirect, request
# from sqlalchemy import update

# @app.route('/')
# def index():
#     colours = []
#     return render_template('index.html', title="Home", colours=colours)

@app.route('/', methods=['GET', 'POST'])
def colours():
    # colours = ['Red', 'Blue', 'Yellow']
    colours = []
    colour = request.form.get('colour')
    colours.append(colour)
    return render_template('index.html', title="Home", colours=colours)

 

