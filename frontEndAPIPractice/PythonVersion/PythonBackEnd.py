from flask import Flask
from flask import render_template
import requests
import json
 
# creates a Flask application
app = Flask(__name__)
  
  
@app.route("/")
def hello():
    response = requests.get('http://dvd-library.us-east-1.elasticbeanstalk.com/dvds').content
    data = json.loads(response)
    return render_template('HTMLFrontEnd.html', data=data)
 
# run the application
if __name__ == "__main__":
    app.run(debug=True)