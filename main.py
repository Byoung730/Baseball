from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://baseball:baseball@localhost:8889/baseball'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class starting_pitchers(db.Model):
    Name = db.Column(db.String(80), unique=True)
    ID = db.Column(db.Integer, primary_key=True)
    CFIP = db.Column(db.Integer)
    xFIP = db.Column(db.Float)
    FIP = db.Column(db.Float)
    KperBB = db.Column(db.Float)
    Total_Ks = db.Column(db.Integer)
    WHIP = db.Column(db.Float)
    ERA = db.Column(db.Float)
    Innings_Pitched = db.Column(db.Float)
    Wins = db.Column(db.Integer)
    Quality_Start_Rate = db.Column(db.Integer)
    Ground_Ball_Rate = db.Column(db.Float)
    Soft_Contact_Rate = db.Column(db.Float)
    FP_Rank = db.Column(db.Integer, unique=True)
    SW_Rank = db.Column(db.Integer)
    CT_Rank = db.Column(db.Integer)
    HC_Rank = db.Column(db.Integer)

    def __init__(self, Name, CFIP, xFIP, FIP, KperBB, Total_Ks, WHIP, ERA, Innings_Pitched, Wins, Quality_Start_Rate,
                 Ground_Ball_Rate, Soft_Contact_Rate, FP_Rank, SW_Rank, CT_Rank, HC_Rank):
        self.Name = Name
        self.CFIP = CFIP
        self.xFIP = xFIP
        self.FIP = FIP
        self.KperBB = KperBB
        self.Total_Ks = Total_Ks
        self.WHIP = WHIP
        self.ERA = ERA
        self.Innings_Pitched = Innings_Pitched
        self.Wins = Wins
        self.Quality_Start_Rate = Quality_Start_Rate
        self.Ground_Ball_Rate = Ground_Ball_Rate
        self.Soft_Contact_Rate = Soft_Contact_Rate
        self.FP_Rank = FP_Rank
        self.SW_Rank = SW_Rank
        self.CT_Rank = CT_Rank
        self.HC_Rank = HC_Rank


@app.route("/", methods=['GET', 'POST'])
def index():
    baseball = starting_pitchers.query.all()

    return render_template('index.html', title="Baseball", baseball=baseball)

'''def algorithm():

    CFIP_Sort = ("SELECT * FROM starting_pitchers ORDER BY CFIP ASC")
    xFIP_Sort = ("SELECT * FROM starting_pitchers ORDER BY xFIP ASC")
    FIP_Sort = ("SELECT * FROM starting_pitchers ORDER BY FIP ASC")
    KperBB_Sort = ("SELECT * FROM starting_pitchers ORDER BY KperBB DESC")
    Total_Ks_Sort = ("SELECT * FROM starting_pitchers ORDER BY Total_Ks DESC")
    WHIP_Sort = ("SELECT * FROM starting_pitchers ORDER BY WHIP ASC")
    ERA_Sort = ("SELECT * FROM starting_pitchers ORDER BY ERA ASC")
    Innings_Pitched_Sort = ("SELECT * FROM starting_pitchers ORDER BY Innings_Pitched DESC")
    Wins_Sort = ("SELECT * FROM starting_pitchers ORDER BY Wins DESC")
    Quality_Start_Rate_Sort = ("SELECT * FROM starting_pitchers ORDER BY Quality_Start_Rate DESC")
    Ground_Ball_Rate_Sort = ("SELECT * FROM starting_pitchers ORDER BY Ground_Ball_Rate DESC")
    Soft_Contact_Rate_Sort = ("SELECT * FROM starting_pitchers ORDER BY Soft_Contact_Rate DESC")
    FP_Rank_Sort = ("SELECT * FROM starting_pitchers ORDER BY FP_Rank ASC")
    SW_Rank_Sort = ("SELECT * FROM starting_pitchers ORDER BY SW_Rank ASC")
    CT_Rank_Sort = ("SELECT * FROM starting_pitchers ORDER BY CT_Rank ASC")
    HC_Rank_Sort = ("SELECT * FROM starting_pitchers ORDER BY HC_Rank ASC")

    return '''

if __name__ == '__main__':
    app.run()
