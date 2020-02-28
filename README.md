# Flask Dropdown App

## Learning Purpose
To learn how to use dropdown menus in Flask. This is something I was having problems with in other apps, so I wanted to isolate the dropdown menu. 

## Features
* Flask, render_template
* HTML `<form>` and `<select>` tags

## What I learned
The `name` variable inside the `<select>` tag (in the html file) has to match the argument you are passing in the relevant function (in the `routes` file).

In the html template where you will render the form:
```
       <form action="/" method="POST">
            <label for="colour">Colour</label>
            <select name="colour">
                    <option disabled selected value> -- select an option -- </option>
                     <option value="red">Red</option><br>
                     <option value="blue">Blue</option><br>
                     <option value="yellow">Yellow</option><br>
                     <option value="green">Green</option><br>
                </select>
            <br>
            <button type="submit" class="btn btn-primary" value="Add Colour">Add Colour</button>
        </form>
```

In `routes.py`: 
```
@app.route('/', methods=['GET', 'POST'])
def colours():
    # colours = ['Red', 'Blue', 'Yellow']
    colours = []
    colour = request.form.get('colour')
    colours.append(colour)
    return render_template('index.html', title="Home", colours=colours)
```