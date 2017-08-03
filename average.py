from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from models import starting_pitchers
from main import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://baseball:baseball@localhost:8889/baseball'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


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

    'dictionary key will be ID, value will be composite average'

    Sorted_avg_dict = {}
    Avg_list = []

    for o in CFIP_sort_list:

        index_collector = (3*CFIP_sort_list.index(o))
        if o in xFIP_sort_list:
            index_collector += xFIP_sort_list.index(o)
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
            index_collector += 3*(FP_Rank_sort_list.index(o))
        if o in SW_Rank_sort_list:
            index_collector += 3*(SW_Rank_sort_list.index(o))
        if o in CT_Rank_sort_list:
            index_collector += 3*(SW_Rank_sort_list.index(o))
        if o in HC_Rank_sort_list:
            index_collector += 3*(HC_Rank_sort_list.index(o))

            Sorted_avg_dict[o.Name] = (index_collector / 26)


    print(Sorted_avg_dict)

    return Sorted_avg_dict

