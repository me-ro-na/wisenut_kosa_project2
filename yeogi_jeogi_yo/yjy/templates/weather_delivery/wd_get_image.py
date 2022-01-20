import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from yjy.templates.weather_delivery import weather_delivery_data
from io import BytesIO
from flask import send_file
import seaborn as sns

def save_img_chart6():
    df = weather_delivery_data.get_chart6()
    ratio = df["Greatest"]
    labels = df["Category"]
    colors = ['#FB9DA7', '#FCCCD4', '#FBDEA2', '#F2E2C6', '#8EB695', '#D9F1F1', '#B6E3E9']
    wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
    sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus": False, "axes.labelsize": 10}, font_scale=1.5)
    
    plt.figure(figsize=(10, 8))
    plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops)

    plt.savefig("yjy/static/images/chart/chart6.png", dpi=300, orientation = 'horizontal')
    plt.close()

def save_img_chart6_sec1():
    df = weather_delivery_data.get_chart6_sec1()
    sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus":False, "grid.linewidth": 0.5, "axes.labelsize": 20}, style="whitegrid", font_scale=1.8)

    plt.figure(figsize=(20, 7))
    plt.barh(df["Address"], df["Sum"], color="#ADD8E6")
    plt.ylabel("Address", fontsize=15)
    plt.xlabel("Sum", fontsize=15)
    plt.yticks(df["Address"], df["Address"], fontsize=13, rotation=0)
    sns.despine(right=True, top=True)

    img = BytesIO()
    plt.savefig(img, format='png', dpi=100)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

def save_img_chart6_sec2(loc, addr):
    df = weather_delivery_data.get_chart6_sec2(loc, addr)
    
    sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus":False, "grid.linewidth": 0.5, "axes.labelsize": 20}, style="whitegrid", font_scale=1.8)
    plt.figure(figsize=(20, 7))

    plt.bar(df["Category"], df["Sum"], color="#F4A460")
    plt.xlabel('Category', fontsize=18)
    plt.ylabel('Sum', fontsize=18)
    plt.xticks(df["Category"], fontsize=15)

    sns.despine(right=True, top=True)

    img = BytesIO()
    plt.savefig(img, format='png', dpi=100)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

