from app import app
from flask import render_template, redirect, request


@app.route('/', methods=['GET', 'POST'])
def colours():
    colours = []
    colour = request.form.get('colour')
    colours.append(colour)
    return render_template('index.html', title="Home", colours=colours)

 

