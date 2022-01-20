import sys
[sys.path.append(i) for i in ['.', '..']]

import pandas as pd
from yeogi_jeogi_yo import DBUtil

def get_chart5():
    db_class = DBUtil.Database()
    sql = """SELECT ADDR2, COUNTING, ROUND(SUM(FREQUENCY))
            FROM HOUSING_TYPE
            WHERE ADDR1 LIKE '서울특별시' AND ADDR2 LIKE '강남구'
            GROUP BY ADDR2, COUNTING
            ORDER BY ADDR2"""
    row = db_class.executeAll(sql)
    return to_df(row)

def get_chart5_sec1(addr):
    db_class = DBUtil.Database()
    sql = f"""SELECT COUNTING, ROUND(SUM(FREQUENCY))
            FROM HOUSING_TYPE
            WHERE ADDR1 LIKE '{addr}'
            GROUP BY COUNTING"""
    row = db_class.executeAll(sql)
    return to_df_sec1(row)

def to_df(list):
    cityList = []
    kindList = []
    numList = []

    for i in list:
        cityList.append(i[0])
        kindList.append(i[1])
        numList.append(i[2])

    df = pd.DataFrame(data={"지역": cityList, "세대구성분류": kindList, "빈도수": numList})
    return df

def to_df_sec1(list):
    kindList = []
    numList = []

    for i in list:
        kindList.append(i[0])
        numList.append(i[1])
    df = pd.DataFrame(data={"세대구성분류": kindList, "빈도수": numList})
    return df

def get_addr():
    db = DBUtil.Database()
    sql = f"""SELECT ADDR1 FROM HOUSING_TYPE
            GROUP BY ADDR1 ORDER BY ADDR1"""
    row = db.executeAll(sql)
    resultList = []

    for i in row:
        resultList.append(i[0])
    return resultList