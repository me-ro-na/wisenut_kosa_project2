import sys
[sys.path.append(i) for i in ['.', '..']]
# 파일 임포트 오류 방지

import pandas as pd
from yeogi_jeogi_yo import DBUtil

def get_chart1_group_cat():
    db_class= DBUtil.Database()
    sql = """SELECT CATEGORY, ROUND(AVG(AVG_PRICE)) AS AVG FROM LUNCH_PRICE GROUP BY CATEGORY"""
    row = db_class.executeAll(sql)
    return to_df(row)

def get_chart1_avg():
    db_class= DBUtil.Database()
    sql = """SELECT CATEGORY, TO_CHAR(BENCH_DATE, 'YYYY-MM') AS MONTH, ROUND(AVG(AVG_PRICE)) AS AVG
            FROM LUNCH_PRICE
            WHERE BENCH_DATE >= TO_DATE('2021.06.01', 'YYYY.MM.DD')
            GROUP BY CATEGORY, BENCH_DATE
            ORDER BY BENCH_DATE, CATEGORY"""
    row = db_class.executeAll(sql)
    return to_df_avg(row)

def get_chart1_sec1(wants):
    db_class= DBUtil.Database()
    sql = """SELECT CATEGORY, TO_CHAR(BENCH_DATE, 'YYYY-MM') AS MONTH, ROUND(AVG(AVG_PRICE)) AS AVG
            FROM LUNCH_PRICE
            WHERE BENCH_DATE >= TO_DATE('2021.06.01', 'YYYY.MM.DD') AND CATEGORY IN ("""

    for i in range(0, len(wants)):
        sql += """'""" + wants[i] + """'"""
        if i < len(wants)-1:
            sql += ", "
    sql += """)
            GROUP BY CATEGORY, BENCH_DATE
            ORDER BY BENCH_DATE, CATEGORY"""
    row = db_class.executeAll(sql)
    return to_df_avg(row)

def to_df(list_2d):
    list1, list2 = [], []
    for i in list_2d:
        list1.append(i[0])
        list2.append(i[1])
    df = pd.DataFrame(data={"Category": list1, "Average": list2})
    return df

def to_df_avg(list_2d):
    list1, list2, list3 = [], [], []
    for i in list_2d:
        list1.append(i[0])
        list2.append(i[1])
        list3.append(i[2])
    df = pd.DataFrame(data={"Category": list1, "Month": list2, "Average": list3})
    return df