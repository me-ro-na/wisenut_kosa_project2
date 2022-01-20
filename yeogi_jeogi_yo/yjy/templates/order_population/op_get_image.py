import seaborn as sns
from matplotlib import pyplot as plt
from yjy.templates.order_population import order_population_data

def save_img_chart4():
    df = order_population_data.get_chart4()

    sns.set(font="NanumGothicCoding", rc={"axes.unicode_minus": False, "grid.linewidth": 0.5, "axes.labelsize": 18}, style="whitegrid", font_scale=0.5)
    plt.figure(figsize=(10, 8))
    plt.bar(df["City"], df["Sum"], color="#ADD8E6")

    sns.despine(right=True, top=True)

    plt.savefig('yjy/static/images/chart/chart4.png', format='png', dpi=300)
    plt.close()