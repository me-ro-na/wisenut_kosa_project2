import sys
[sys.path.append(i) for i in ['.', '..']]

from yeogi_jeogi_yo import DBUtil

def get_data():
    db_class= DBUtil.Database()
    sql = "SELECT * FROM mango ORDER BY RANK"
    row = db_class.executeAll(sql)
    return row

def get_popular_list():
    result = []
    db_class= DBUtil.Database()
    sql = "SELECT NAME, SECTORS||'('||ADDRESS||')' FROM mango ORDER BY RANK"
    row = db_class.executeAll(sql)
    for i in row:
        temp = i[0].split('\n')
        result.append(temp[0] + ' - ' + i[1])
    return result