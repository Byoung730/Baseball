from main import db


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

    def __init__(self, ID):
        self.ID = ID
