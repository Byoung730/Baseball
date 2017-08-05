from flask_sqlalchemy import SQLAlchemy
from models import starting_pitchers
from db import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app

engine = create_engine('mysql+pymysql://baseball:baseball@localhost:8889/baseball', echo=True)
# Session = sessionmaker(bind=engine)


def average():
    CFIP_sort_list = []
    for i in starting_pitchers.query.order_by('CFIP asc'):
        CFIP_sort_list.append(i)
    xFIP_sort_list = []
    for ii in starting_pitchers.query.order_by('xFIP asc'):
        xFIP_sort_list.append(ii)
    FIP_sort_list = []
    for iii in starting_pitchers.query.order_by('FIP asc'):
        FIP_sort_list.append(iii)
    KperBB_sort_list = []
    for iv in starting_pitchers.query.order_by('KperBB desc'):
        KperBB_sort_list.append(iv)
    Total_Ks_sort_list = []
    for v in starting_pitchers.query.order_by('Total_Ks desc'):
        Total_Ks_sort_list.append(v)
    WHIP_sort_list = []
    for vi in starting_pitchers.query.order_by('WHIP asc'):
        WHIP_sort_list.append(vi)
    ERA_sort_list = []
    for vii in starting_pitchers.query.order_by('ERA asc'):
        ERA_sort_list.append(vii)
    IP_sort_list = []
    for viii in starting_pitchers.query.order_by('Innings_Pitched desc'):
        IP_sort_list.append(viii)
    Wins_sort_list = []
    for ix in starting_pitchers.query.order_by('Wins desc'):
        Wins_sort_list.append(ix)
    QS_Rate_sort_list = []
    for x in starting_pitchers.query.order_by('Quality_Start_Rate desc'):
        QS_Rate_sort_list.append(x)
    GB_Rate_sort_list = []
    for xi in starting_pitchers.query.order_by('Ground_Ball_Rate desc'):
        GB_Rate_sort_list.append(xi)
    SC_Rate_sort_list = []
    for xii in starting_pitchers.query.order_by('Soft_Contact_Rate desc'):
        SC_Rate_sort_list.append(xii)
    FP_Rank_sort_list = []
    for xiii in starting_pitchers.query.order_by('FP_Rank asc'):
        FP_Rank_sort_list.append(xiii)
    SW_Rank_sort_list = []
    for xiii in starting_pitchers.query.order_by('SW_Rank asc'):
        SW_Rank_sort_list.append(xiii)
    CT_Rank_sort_list = []
    for xiv in starting_pitchers.query.order_by('CT_Rank asc'):
        CT_Rank_sort_list.append(xiv)
    HC_Rank_sort_list = []
    for xv in starting_pitchers.query.order_by('HC_Rank asc'):
        HC_Rank_sort_list.append(xv)

    Sorted_avg_dict = {}

    for o in CFIP_sort_list:

        index_collector = (3 * CFIP_sort_list.index(o))
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
            index_collector += 3 * (FP_Rank_sort_list.index(o))
        if o in SW_Rank_sort_list:
            index_collector += 3 * (SW_Rank_sort_list.index(o))
        if o in CT_Rank_sort_list:
            index_collector += 3 * (SW_Rank_sort_list.index(o))
        if o in HC_Rank_sort_list:
            index_collector += 3 * (HC_Rank_sort_list.index(o))

            Sorted_avg_dict[o.Name] = (index_collector / 26)

        print(Sorted_avg_dict)

    return Sorted_avg_dict


if __name__ == "__main__":
    db.app = app
    average()
