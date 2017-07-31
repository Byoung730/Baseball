import pypyodbc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://baseball:baseball@localhost:8889/baseball'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# creating connection Object which will contain SQL Server Connection
connection = pypyodbc.connect('Driver={SQL Server};Server=localhost;Database=baseball;uid=baseball;baseball')

class Baseball(db.Model):
    __tablename__ = 'starting_pitchers'

    Name = db.Column(db.String(80), unique=True)
    ID = db.Column(db.Integer, primary_key=True)
    CFIP = db.Column(db.Integer)
    xFIP = db.Column(db.double)
    FIP = db.Column(db.float)
    KperBB = db.Column(db.float)
    Total_Ks = db.Column(db.Integer)
    WHIP = db.Column(db.float)
    ERA = db.Column(db.float)
    Innings_Pitched = db.Column(db.float)
    Wins = db.Column(db.Integer)
    Quality_Start_Rate = db.Column(db.Integer)
    Swinging_Strike_Rate = db.Column(db.float)
    Ground_Ball_Rate = db.Column(db.float)
    Soft_Contact_Rate = db.Column(db.float)
    FP_Rank = db.Column(db.Integer, unique=True)
    SW_Rank = db.Column(db.Integer)
    CT_Rank = db.Column(db.Integer)
    HC_Rank = db.Column(db.Integer)

    def __init__(self, ID, name):
        self.name = name
        self.ID = ID

# Creating Cursor
cursor = connection.cursor()
cursor.execute("SELECT * FROM starting_pitchers")
s = "<table style='border:1px solid red'>"
for row in cursor:
    s = s + "<tr>"
for x in row:
    s = s + "<td>" + str(x) + "</td>"
s = s + "</tr>"

connection.close()


@app.route("/", methods=['GET', 'POST'])
def index():

    return ("index.html")