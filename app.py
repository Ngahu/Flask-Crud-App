"""
Description:This scripts basically create a flask app
"""
from flask import Flask,render_template


app = Flask(__name__)



@app.route('/')
def index():
    """
    Description:Render the home route.
    """
    return render_template('home.html')




if __name__ == "__main__":
    app.run(debug=True)