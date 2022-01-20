from re import split
import sys
[sys.path.append(i) for i in ['.', '..']]
# 파일 임포트 오류 방지

import pandas as pd
from yeogi_jeogi_yo import DBUtil

def get_chart6():
    db_class= DBUtil.Database()
    sql = """SELECT SUM(KOR_FOOD), SUM(BOONSIK_FOOD), SUM(DESERT_FOOD), SUM(PORK_CUTLET_FOOD), SUM(SASIMI_FOOD),
                SUM(CHICKEN_FOOD), SUM(PIZZA_FOOD), SUM(EAST_ASIA_FOOD), SUM(CHN_FOOD), SUM(BOSSAM_JOK_FOOD),
                SUM(MIDNIGHT_FOOD), SUM(SOUP_FOOD), SUM(DOSIRAK_FOOD), SUM(FAST_FOOD)
            FROM WEATHER_DELIVERY
            WHERE IS_RAIN = 'T'"""
    row = db_class.executeAll(sql)
    return to_df(row)

def get_chart6_sec1():
    db_class = DBUtil.Database()
    sql = """SELECT ADDR3, SUM(KOR_FOOD)+SUM(BOONSIK_FOOD)+SUM(DESERT_FOOD)+SUM(PORK_CUTLET_FOOD)+SUM(SASIMI_FOOD)
                +SUM(CHICKEN_FOOD)+SUM(PIZZA_FOOD)+SUM(EAST_ASIA_FOOD)+SUM(CHN_FOOD)+SUM(BOSSAM_JOK_FOOD)
                +SUM(MIDNIGHT_FOOD)+SUM(SOUP_FOOD)+SUM(DOSIRAK_FOOD)+SUM(FAST_FOOD) AS SUM
            FROM WEATHER_DELIVERY
            WHERE IS_RAIN = 'T'
            GROUP BY ADDR3
            ORDER BY SUM DESC"""
    row = db_class.executeAll(sql)
    return to_df_sec1(row)

def get_chart6_sec2(loc, addr):
    db_class = DBUtil.Database()
    sql = f"""SELECT {loc}, SUM(KOR_FOOD), SUM(BOONSIK_FOOD), SUM(DESERT_FOOD), SUM(PORK_CUTLET_FOOD), SUM(SASIMI_FOOD),
                SUM(CHICKEN_FOOD), SUM(PIZZA_FOOD), SUM(EAST_ASIA_FOOD), SUM(CHN_FOOD), SUM(BOSSAM_JOK_FOOD),
                SUM(MIDNIGHT_FOOD), SUM(SOUP_FOOD), SUM(DOSIRAK_FOOD), SUM(FAST_FOOD)
            FROM WEATHER_DELIVERY
            WHERE {loc} = '{addr}' GROUP BY {loc}"""
    row = db_class.executeAll(sql)
    return to_df_sec2(row)

def get_addr1():
    db_class = DBUtil.Database()
    sql = """SELECT ADDR1 FROM WEATHER_DELIVERY GROUP BY ADDR1 ORDER BY ADDR1"""
    row = db_class.executeAll(sql)
    result = []
    for i in row:
        for j in i:
            result.append(j)
    return result

def get_addr2(addr1):
    db_class = DBUtil.Database()
    sql = f"""SELECT ADDR2 FROM WEATHER_DELIVERY WHERE ADDR1 = '{addr1}' GROUP BY ADDR2 ORDER BY ADDR2"""
    row = db_class.executeAll(sql)
    result = []
    for i in row:
        for j in i:
            result.append(j)
    return result

def to_df_sec2(list_2d):
    catList, sumList = get_foods(), list_2d[0][1:]
    return {"Category": catList, "Sum": sumList}

def to_df_sec1(list_2d):
    addrList, sumList = [], []
    for i in list_2d:
        addrList.append(i[0])
        sumList.append(i[1])
    df = {"Address": addrList, "Sum": sumList}
    return df

def to_df(list_2d):
    maxList, catList = list_2d[0], get_foods()
    df = pd.DataFrame(data={"Greatest": maxList, "Category": catList})
    return df

def get_foods():
    db_class = DBUtil.Database()
    sql = """SELECT ROWNUM AS NUM, COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = 'WEATHER_DELIVERY'"""
    row = db_class.executeAll(sql)
    row = to_list(row)
    result = []
    dic = {"KOR_FOOD": "한식", "BOONSIK_FOOD": "분식", "DESERT_FOOD": "디저트", "PORK_CUTLET_FOOD": "돈까스", "SASIMI_FOOD": "회", "CHICKEN_FOOD": "치킨", "PIZZA_FOOD": "피자", "EAST_ASIA_FOOD": "동아시아", "CHN_FOOD": "중식", "BOSSAM_JOK_FOOD": "보쌈", "MIDNIGHT_FOOD": "야식", "SOUP_FOOD": "죽", "DOSIRAK_FOOD": "도시락", "FAST_FOOD": "패스트푸드"}
    for i in range(8, len(row)):
        result.append(dic[row[i]])
    return result

def to_list(list_2d):
    result = []
    for i in list_2d:
        result.append(i[1])
    return result