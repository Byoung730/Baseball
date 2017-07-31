from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///tmp/test.db', convert_unicode=True)
metadata = MetaData(bind=engine)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://baseball:baseball@localhost:8889/baseball'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
@app.route('/')
def index():

        starting_pitchers = Table('starting_pitchers', metadata, autoload=True)
        baseball = [i for i in starting_pitchers.query.all()]
        return render_template('index.html', title='Home', baseball=baseball)

if __name__ == '__main__':
    app.run(debug=True)