"""
Description:This scripts basically create a flask app
"""
from flask import (
        Flask,
        render_template,
        flash,
        redirect,
        url_for,
        session,llogging
        )


from flask_mysqldb import MySQL
from wtforms import (
                    Form,
                    StringField,
                    TextAreaField,
                    PasswordField,
                    validators
                    )

from passlib.hash import  sha256_crypt

from data import all_articles

app = Flask(__name__)
mysql = MySQL(app)

Articles = all_articles()

@app.route('/')
def index():
    """
    Description:Render the home route.
    """
    return render_template('home.html')





@app.route('/about')
def about():
    """
    Description:Render the about page .
    """
    return render_template('about.html')



@app.route('/articles')
def articles():
    """
    Description:Render the articles page .
    """
    return render_template('articles.html',articles=Articles)



@app.route('/articles/<string:id>/')
def article_detail(id):
    """
    Description:Render the articles page .
    """
    return render_template('article_detail.html',id=id)







# forms


class RegisterForm(Form):
    """
    Description:This is the form that is going to be used by the user to register.\n
    """
    name = StringField('Name',[validators.Length(min=1,max=50)])
    username = StringField('Username',[validators.Length(min=4,max=27)])
    email = StringField('Email',[validators.Length(min=4,max=57)])
    password = PasswordField('Password',[
                validators.DataRequired(),
                validators.EqualTo('confirm',message='Passwords do not match.')

    ])
    confirm = PasswordField('Confirm Password')


if __name__ == "__main__":
    app.run(debug=True)