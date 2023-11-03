#3) to use URL parameters to display dynamic content

# Importing required functions 
from flask import Flask, request

# Flask constructor 
app = Flask(__name__)

# Single URL Converter 


@app.get('/home/<menu>')
def single_converter(menu):

	return "You tried accessing 'single_converter' \
	endpoint with value of 'menu' as " + str(menu)


# Main Driver Function 
if __name__ == '__main__':
	# Run the application on the local development server
	app.run(debug=True)
