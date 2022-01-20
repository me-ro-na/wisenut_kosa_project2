#-*-coding:utf-8-*-
import pandas as pd

import sys
[sys.path.append(i) for i in ['.', '..']]

from yeogi_jeogi_yo import DBUtil

def get_chart4():
    db = DBUtil.Database()

    sql = """SELECT ADDR1, (SUM(MALE_POPULATION)+SUM(FEMALE_POPULATION)) AS A, SUM(MALE_POPULATION), SUM(FEMALE_POPULATION)
            FROM POPULATION_TYPE
            GROUP BY ADDR1
            ORDER BY ADDR1"""
    row = db.executeAll(sql)
    return to_df(row)

def to_df(list):
    cityList, sumList , maleList, femaleList= [], [], [], []
    for i in list:
        cityList.append(i[0])
        sumList.append(i[1])
        maleList.append(i[2])
        femaleList.append(i[3])
    df = pd.DataFrame(data={"City": cityList, "Sum": sumList, "male": maleList, "female": femaleList})
    return df