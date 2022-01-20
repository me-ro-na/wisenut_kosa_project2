import sys
[sys.path.append(i) for i in ['.', '..']]
from yeogi_jeogi_yo import DBUtil

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def save_img_chart2():
    sql = """SELECT del_level, gender, dels_sum FROM DELIVERY_PATTERN"""
    row = DBUtil.Database().executeAll(sql)
    df = pd.DataFrame(row)
    df.rename(columns={0: '선호경향', 1: '성별', 2: '합계'}, inplace=True)

    sns.set(font="NanumGothicCoding",
            rc={"figure.figsize": (20, 10), "axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 10},
            style="whitegrid", font_scale=1)
    result = sns.lmplot(x='선호경향', y='합계', hue='성별', data=df)
    plt.savefig("yjy/static/images/chart/chart2.png", dpi=300, orientation = 'horizontal')
    plt.close()

def get_chart2_hl():
    sql = """SELECT health_level, gender, dels_sum FROM DELIVERY_PATTERN"""
    row = DBUtil.Database().executeAll(sql)
    df = pd.DataFrame(row)
    df.rename(columns={0: '건강관심도', 1: '성별', 2: '합계'}, inplace=True)

    sns.set(font="NanumGothicCoding",
            rc={"figure.figsize": (20, 7), "axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 10},
            style="whitegrid", font_scale=1)
    result = sns.lmplot(x='건강관심도', y='합계', hue='성별', data=df)
    plt.savefig("yjy/static/images/chart/chart2_1.png", dpi=300, orientation='horizontal')
    plt.close()

