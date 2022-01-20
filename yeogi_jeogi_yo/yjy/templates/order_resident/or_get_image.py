from matplotlib import pyplot as plt
import seaborn as sns
from yjy.templates.order_resident import order_resident_data
from io import BytesIO
from flask import send_file

def save_img_chart5():
        df = order_resident_data.get_chart5()

        sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 18}, style="whitegrid", font_scale=1.3)
        plt.figure(figsize=(10, 8))

        ratio = df['빈도수']
        labels = df['세대구성분류']
        colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', '#2E8B57', '#87CEEB', '#DDA0DD', '#778899']
        wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

        plt.rc('font', family='NanumGothicCoding')
        plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops)

        plt.savefig('yjy/static/images/chart/chart5.png', format='png', dpi=300)
        plt.close()

def save_img_chart5_sec1(addr):
        df = order_resident_data.get_chart5_sec1(addr)

        sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 18}, style="whitegrid", font_scale=1.3)

        plt.figure(figsize=(13, 8))

        ratio = df['빈도수']
        labels = df['세대구성분류']
        colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', '#2E8B57', '#87CEEB', '#DDA0DD', '#778899']
        wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

        plt.rc('font', family='NanumGothicCoding')
        plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops)

        img = BytesIO()
        plt.savefig(img, format='png', dpi=100)
        img.seek(0)
        plt.close()
        return send_file(img, mimetype='image/png')