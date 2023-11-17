from flask import Flask, request, render_template
import requests # Import the requests module

# TODO: Stretch Challenges 2
# The homeworld property is a URL to the homeworl at the SWAPI. 
# Make another request and get the homeworld data and display the name of the hoemworld.


# TODO Stretch Challenge 3
#Displaying Lists
#Every character has a films property that is a list of the films they appeared in. 
# This list is a list of URLs to those films on SWAPI. Loop over this list, 
# make a request to get the data for each film and display the name of each film.

# TODO Style your work. This is open ended put as much time into this as you like.
# Style the form elements and the the output data.

app = Flask(__name__, template_folder="templates")

SWAPI_URL = 'https://swapi.py4e.com/api/'

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/swapi_results', methods=['GET', 'POST'])
def swapi_results():
    """Show a form to search for Star Wars Characters and show resulting character attributes."""
    if request.method == 'POST':
        # Get category and id from the form.
        category = request.form.get('category')
        item_id = request.form.get('id')

        # Make a reqest to SWAPI to get data
        response = requests.get(f'{SWAPI_URL}{category}/{item_id}/')

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response received from SWAPI
            data = response.json()
            
            context = {
            'data': data,
            }

            return render_template('swapi_results.html', **context)
        else:
            # Handle the case where the item ID was not found
            context = {
            'error_message': 'Character not found🫠'
            }

            return render_template('swapi_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
