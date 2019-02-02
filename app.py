"""
Description:This scripts basically create a flask app
"""
from flask import Flask,render_template
from data import all_articles

app = Flask(__name__)


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





if __name__ == "__main__":
    app.run(debug=True)