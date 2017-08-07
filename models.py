from db import db

class starting_pitchers(db.Model):
    __tablename__ = 'starting_pitchers'
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


class Composite_Rank(db.Model):
    __tablename__ = 'Composite_Rank'
    C_Name = db.Column(db.String(80), unique=True, primary_key=True)
    C_Rank = db.Column(db.Float)

    def __init__(self, C_Name, C_Rank):
        self.C_Name = C_Name
        self.C_Rank = C_Rank