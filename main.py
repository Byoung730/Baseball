from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import jinja2, os, re
from models import Stats

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://baseball:baseball@localhost:8889/baseball'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)



template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)



@app.route("/", methods=['GET','POST'])
def index():

    def get_stats(self, limit, offset):
        """ Get all stats for display table """
        query = baseball.all()
        return query.fetch()

    return render_template('index.html', title="baseball")

if __name__ == '__main__':
    app.run()