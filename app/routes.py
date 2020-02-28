from app import app
from flask import render_template, redirect, request


@app.route('/', methods=['GET', 'POST'])
def select_colour():
    selected_colour = []
    colour = request.form.get('colour')
    selected_colour.append(colour)
    pretty_selected_colour = selected_colour[0]
    return render_template('index.html', title="Home", pretty_selected_colour=pretty_selected_colour)

 

