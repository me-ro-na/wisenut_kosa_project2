import sys
[sys.path.append(i) for i in ['.', '..']]
# 파일 임포트 오류 방지

import pandas as pd
from yeogi_jeogi_yo import DBUtil


# 가장 많이 팔리는 음식(치킨)이 몇시인지
def get_chart3():
    db_class= DBUtil.Database()
    sql = """SELECT TO_CHAR(BENCH_DATE, 'D') AS D, TO_CHAR(BENCH_DATE, 'DY'), CATEGORY
            FROM LOC_DAY_DELIVERY
            WHERE CATEGORY LIKE (SELECT CATEGORY FROM(
                    SELECT CATEGORY, COUNT(CATEGORY) AS CNT
                    FROM LOC_DAY_DELIVERY
                    GROUP BY CATEGORY
                    ORDER BY CNT DESC
                ) WHERE ROWNUM = 1
            )
            ORDER BY D"""
    row = db_class.executeAll(sql)
    return to_df(row)

# 음식이 어느 요일, 어느 시간에 가장 많이 팔리는지
def get_chart3_sec1(cats):
    db_class= DBUtil.Database()
    sql = """SELECT TO_CHAR(BENCH_DATE, 'D') AS BEN_DATE, TO_CHAR(BENCH_DATE, 'DAY') AS BEN_DATE_2, TO_CHAR(BENCH_DATE, 'HH24')||'시' AS BEN_HOUR,
                COUNT(CATEGORY) AS CNT
            FROM LOC_DAY_DELIVERY
            WHERE CATEGORY IN("""
    for i in cats:
        sql += """'""" + i + """'"""
        if i != cats[len(cats)-1]:
            sql += ", "
    sql += """)
            GROUP BY TO_CHAR(BENCH_DATE, 'D'), TO_CHAR(BENCH_DATE, 'DAY'), TO_CHAR(BENCH_DATE, 'HH24')
            ORDER BY BEN_DATE, BEN_HOUR"""
    row = db_class.executeAll(sql)
    return to_df_sec1(row)

def get_cats():
    db_class= DBUtil.Database()
    sql = """SELECT CATEGORY FROM LOC_DAY_DELIVERY WHERE CATEGORY NOT IN ('배달전문업체', '심부름') GROUP BY CATEGORY ORDER BY CATEGORY"""
    row = db_class.executeAll(sql)
    result = []
    for i in row:
        for j in i:
            result.append(j)
    return result

def to_df(list_2d):
    list1 = []
    best_menu = list_2d[0][2]
    for i in list_2d:
        list1.append(i[1])
    df = pd.DataFrame(data={"Day": list1, "Category": best_menu})
    return df

def to_df_sec1(list_2d):
    list1, list2, list3 = [], [], []
    for i in list_2d:
        list1.append(i[1])
        list2.append(i[2])
        list3.append(i[3])
    df = pd.DataFrame(data={"Date": list1, "Hour": list2, "Count": list3})
    return df