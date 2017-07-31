import jinja2, os, re
from models import Baseball
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://baseball:baseball@localhost:8889/baseball'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

@app.route("/", methods=['GET', 'POST'])
def index():

    def connect_db():
        """Connects to the specific database."""
        Baseball = sqlite3.connect(app.config['Baseball'])
        Baseball.row_factory = sqlite3.Row
        return Baseball

    def get_db():
        if not hasattr(g, 'sqlite_db'):
            g.sqlite_db = connect_db()
        return g.sqlite_db



if __name__ == '__main__':
    app.run()