from flask import Flask, render_template
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


@app.route("/", methods=['GET'])
def index():
    baseball = starting_pitchers.query.all()

    def avgs():

        CFIP_sort_list = starting_pitchers.query.order_by('CFIP asc')
        xFIP_sort_list = starting_pitchers.query.order_by('xFIP asc')
        FIP_sort_list = starting_pitchers.query.order_by('FIP asc')
        KperBB_sort_list = starting_pitchers.query.order_by('KperBB desc')
        Total_Ks_sort_list = starting_pitchers.query.order_by('Total_Ks desc')
        WHIP_sort_list = starting_pitchers.query.order_by('WHIP asc')
        ERA_sort_list = starting_pitchers.query.order_by('ERA asc')
        IP_sort_list = starting_pitchers.query.order_by('Innings_Pitched desc')
        Wins_sort_list = starting_pitchers.query.order_by('Wins desc')
        QS_Rate_sort_list = starting_pitchers.query.order_by('Quality_Start_Rate desc')
        GB_Rate_sort_list = starting_pitchers.query.order_by('Ground_Ball_Rate desc')
        SC_Rate_sort_list = starting_pitchers.query.order_by('Soft_Contact_Rate desc')
        FP_Rank_sort_list = starting_pitchers.query.order_by('FP_Rank asc')
        SW_Rank_sort_list = starting_pitchers.query.order_by('SW_Rank asc')
        CT_Rank_sort_list = starting_pitchers.query.order_by('CT_Rank asc')
        HC_Rank_sort_list = starting_pitchers.query.order_by('HC_Rank asc')

        'dictionary key will be name, value will be composite average'

        Sorted_avg = ()

        for o in CFIP_sort_list:

            index_collector = (3 * CFIP_sort_list.index(o))
            if o in xFIP_sort_list:
                index_collector += xFIP_sort_list.index(o)
                print('yes')
            if o in FIP_sort_list:
                index_collector += FIP_sort_list.index(o)
            if o in KperBB_sort_list:
                index_collector += KperBB_sort_list.index(o)
            if o in Total_Ks_sort_list:
                index_collector += Total_Ks_sort_list.index(o)
            if o in WHIP_sort_list:
                index_collector += WHIP_sort_list.index(o)
            if o in ERA_sort_list:
                index_collector += ERA_sort_list.index(o)
            if o in IP_sort_list:
                index_collector += IP_sort_list.index(o)
            if o in Wins_sort_list:
                index_collector += WHIP_sort_list.index(o)
            if o in QS_Rate_sort_list:
                index_collector += QS_Rate_sort_list.index(o)
            if o in GB_Rate_sort_list:
                index_collector += GB_Rate_sort_list.index(o)
            if o in SC_Rate_sort_list:
                index_collector += SC_Rate_sort_list.index(o)
            if o in FP_Rank_sort_list:
                index_collector += 3 * (FP_Rank_sort_list.index(o))
            if o in SW_Rank_sort_list:
                index_collector += 3 * (SW_Rank_sort_list.index(o))
            if o in CT_Rank_sort_list:
                index_collector += 3 * (SW_Rank_sort_list.index(o))
            if o in HC_Rank_sort_list:
                index_collector += 3 * (HC_Rank_sort_list.index(o))

            Sorted_avg.append(index_collector / 26)

        print('Sorted_avg')

    print('maybe')

    return render_template('index.html', title="Baseball", baseball=baseball)

@app.route("/cfip", methods=['GET'])
def CFIP_page():

    cfip_page = starting_pitchers.query.order_by('CFIP asc')

    return render_template('cfip.html', title='CFIP', cfip_page=cfip_page)

@app.route("/xfip", methods=['GET'])
def xFIP_page():

    xfip_page = starting_pitchers.query.order_by('xFIP asc')

    return render_template('xfip.html', title='xFIP', xfip_page=xfip_page)


@app.route("/fip", methods=['GET'])
def FIP_page():

    fip_page = starting_pitchers.query.order_by('FIP asc')

    return render_template('fip.html', title='FIP', fip_page=fip_page)

@app.route("/kperbb", methods=['GET'])
def kperbb_page():

    kperbb_page = starting_pitchers.query.order_by('KperBB desc')

    return render_template('kperbb.html', title='FIP', kperbb_page=kperbb_page)

@app.route("/total_ks", methods=['GET'])
def total_ks_page():

    total_ks_page = starting_pitchers.query.order_by('Total_Ks desc')

    return render_template('total_ks.html', title='Total Ks', total_ks_page=total_ks_page)

@app.route("/name", methods=['GET'])
def name_page():

    name_page = starting_pitchers.query.order_by('Name asc')

    return render_template('name.html', title='Name', name_page=name_page)

@app.route("/whip", methods=['GET'])
def WHIP_page():

    whip_page = starting_pitchers.query.order_by('WHIP asc')

    return render_template('whip.html', title='WHIP', whip_page=whip_page)

@app.route("/era", methods=['GET'])
def ERA_page():

    era_page = starting_pitchers.query.order_by('ERA asc')

    return render_template('era.html', title='ERA', era_page=era_page)

@app.route("/ip", methods=['GET'])
def IP_page():

    ip_page = starting_pitchers.query.order_by('Innings_Pitched desc')

    return render_template('ip.html', title='Innings Pitched', ip_page=ip_page)

@app.route("/wins", methods=['GET'])
def wins_page():

    wins_page = starting_pitchers.query.order_by('Wins desc')

    return render_template('wins.html', title='Wins', wins_page=wins_page)

@app.route("/qs_rate", methods=['GET'])
def qs_rate_page():

    qs_rate_page = starting_pitchers.query.order_by('Quality_Start_Rate desc')

    return render_template('qs_rate.html', title='Quality Start Rate', qs_rate_page=qs_rate_page)

@app.route("/gb_rate", methods=['GET'])
def gb_rate_page():

    gb_rate_page = starting_pitchers.query.order_by('Ground_Ball_Rate desc')

    return render_template('gb_rate.html', title='Ground Ball Rate', gb_rate_page=gb_rate_page)

@app.route("/sc_rate", methods=['GET'])
def sc_rate_page():

    sc_rate_page = starting_pitchers.query.order_by('Soft_Contact_Rate desc')

    return render_template('sc_rate.html', title='Soft Contact Rate', sc_rate_page=sc_rate_page)

@app.route("/fp_rank", methods=['GET'])
def fp_rank_page():

    fp_rank_page = starting_pitchers.query.order_by('FP_Rank asc')

    return render_template('fp_rank.html', title='FantasyPros Rank', fp_rank_page=fp_rank_page)

@app.route("/sw_rank", methods=['GET'])
def sw_rank_page():

    sw_rank_page = starting_pitchers.query.order_by('SW_Rank asc')

    return render_template('sw_rank.html', title='Scott White Rank', sw_rank_page=sw_rank_page)

@app.route("/ct_rank", methods=['GET'])
def ct_rank_page():

    ct_rank_page = starting_pitchers.query.order_by('CT_Rank asc')

    return render_template('ct_rank.html', title='Chris Towers Rank', ct_rank_page=ct_rank_page)

@app.route("/hc_rank", methods=['GET'])
def hc_rank_page():

    hc_rank_page = starting_pitchers.query.order_by('HC_Rank asc')

    return render_template('hc_rank.html', title='Heath Cummings Rank', hc_rank_page=hc_rank_page)


if __name__ == '__main__':
    app.run()
