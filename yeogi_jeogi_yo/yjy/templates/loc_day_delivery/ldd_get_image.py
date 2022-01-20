import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from yjy.templates.loc_day_delivery import loc_day_delivery_data
from io import BytesIO
from flask import send_file
import seaborn as sns

def save_img_chart3():
    df = loc_day_delivery_data.get_chart3()
    sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 18}, style="whitegrid", font_scale=1.6)
    plt.figure(figsize=(10, 8))
    sns.histplot(data=df, x="Day", kde=True, color="#88B04B", bins=40)

    plt.savefig("yjy/static/images/chart/chart3.png", dpi=300, orientation = 'horizontal')
    plt.close()
    return df["Category"][0]

def save_img_chart3_sec1(cats):
    df = loc_day_delivery_data.get_chart3_sec1(cats)
    date = df["Date"]
    hour = df["Hour"]
    count = df["Count"]
    sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 10}, style="whitegrid", font_scale=1.5)
    plt.figure(figsize=(25, 10))
    plt.scatter(hour, date, count, c="#F2E2C6", alpha=0.8)

    img = BytesIO()
    plt.savefig(img, format='png', dpi=100)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')