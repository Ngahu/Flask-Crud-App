"""
Description:This scripts basically create a flask app
"""


from flask import Flask


app = Flask(__name__)



@app.route('/')
def index():
    """
    Description:Render the home route.
    """
    return 'INDEX HOME'




if __name__ == "__main__":
    app.run(debug=True)