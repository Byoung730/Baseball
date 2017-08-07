from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import starting_pitchers, Composite_Rank

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://baseball:baseball@localhost:8889/baseball'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

@app.route("/", methods=['GET'])
def index():
    baseball = starting_pitchers.query.all()
    composite_rank = Composite_Rank.query.order_by('C_Rank asc')

    return render_template('index.html', title="Baseball", baseball=baseball, composite_rank=composite_rank)

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
