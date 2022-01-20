import seaborn as sns
from yjy.templates.lunch_price import lunch_price_data
from io import BytesIO
from flask import send_file
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def save_img_chart1():
    df = lunch_price_data.get_chart1_avg()
    sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 18}, style="whitegrid", font_scale=1.8)
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x="Month", y="Average", data=df)
    sns.lineplot(x="Month", y="Average", markers=True, dashes=False, hue="Category", data=df)
    plt.legend(loc="lower right", prop={'size': 8})
    sns.despine(left=True, bottom=True)

    plt.savefig("yjy/static/images/chart/chart1.png", dpi=300, orientation = 'horizontal')
    plt.close()

def save_img_chart1_sec1(wants):
    arr = wants.split(",")
    arr[0] = arr[0][1:]
    del arr[len(arr)-1]
    df = lunch_price_data.get_chart1_sec1(arr)
    sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 20}, style="whitegrid", font_scale=1.8)
    plt.figure(figsize=(25, 10))
    sns.scatterplot(x="Month", y="Average", data=df)
    sns.lineplot(x="Month", y="Average", markers=True, dashes=False, hue="Category", data=df)
    plt.legend(bbox_to_anchor=(1, 1), prop={'size': 8})

    sns.despine(left=True, bottom=True)

    chart1_img = BytesIO()
    plt.savefig(chart1_img, format='png', dpi=100)
    chart1_img.seek(0)
    plt.close()
    return send_file(chart1_img, mimetype='image/png')
