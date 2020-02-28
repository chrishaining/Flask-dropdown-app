# Flask Dropdown App

## Learning Purpose
To learn how to use dropdown menus in Flask. This is something I was having problems with in other apps, so I wanted to isolate the dropdown menu. 

## Features
* Flask, render_template
* HTML `<form>` and `<select>` tags

## What I learned
The `name` variable inside the `<select>` tag (in the html file) has to match the argument you are passing in the relevant function (in the `routes` file). So, in `index.html` below there is a line `<select name="colour">`, and this matches the line `colour = request.form.get('colour')` in `routes.py`.

In the html template where you will render the form (`index.html`):
```
       <form action="/" method="POST"> # action tells which route to use; method states you are posting something
            <select name="colour"> # this is where you give the argument to pass into the form
                    <option disabled selected value> -- select an option -- </option> # give a default blank option
                     <option value="red">Red</option> # the value in the options is the content of what will be passed to the form
                     <option value="blue">Blue</option>
                     <option value="yellow">Yellow</option>
                     <option value="green">Green</option>
                </select>
            <button type="submit" class="btn btn-primary" value="Add Colour">Add Colour</button> # you submit the form with this button
        </form>
```
What this means:

In `routes.py`: 
```
@app.route('/', methods=['GET', 'POST'])
def select_colour():
    selected_colour = [] # create an empty list 
    colour = request.form.get('colour') # get the name from the form you created in the html file
    selected_colour.append(colour) # attach the colour to selected_colour
    pretty_selected_colour = selected_colour[0] # not essential, but here you are making sure you show a string rather than the whole list.
    return render_template('index.html', title="Home", pretty_selected_colour=pretty_selected_colour) # what you are rendering
```

It is a bit strange that selected_colour is a list, given that it's always going to be one item. However, it works. Perhaps there is a better data type to use - I can look into that another time.