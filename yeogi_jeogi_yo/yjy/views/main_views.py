from flask import Blueprint, render_template, request

from yjy.templates.weather_delivery import weather_delivery_data, wd_get_image
from yjy.templates.lunch_price import lp_get_image, lunch_price_data
from yjy.templates.delivery_pattern import dp_get_image
from yjy.templates.loc_day_delivery import loc_day_delivery_data, ldd_get_image
from yjy.templates.order_population import order_population_data, op_get_image
from yjy.templates.order_resident import order_resident_data, or_get_image
from yjy.templates.mango import mango_get_data

from importlib import reload
import datetime

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    lp_get_image.save_img_chart1()
    dp_get_image.save_img_chart2()
    cat = ldd_get_image.save_img_chart3()
    op_get_image.save_img_chart4()
    or_get_image.save_img_chart5()
    wd_get_image.save_img_chart6()
    return render_template('index.html', chart3_cat=cat)

# 서브페이지
@bp.route('/mango')
def mango():
    from yjy.templates.mango import crawling_mango
    data = mango_get_data.get_data()
    dt = datetime.datetime.now()
    fileName = f"Mango_{dt.year}_{dt.month}_{dt.day}" + '.csv'
    return render_template('mango/mango_list.html', data=data, fileName=fileName)

@bp.route('/chart1')
def chart1():
    cats = lunch_price_data.get_chart1_group_cat()['Category']
    checks = ["primary", "success", "info", "danger", "warning"]
    if cats.size > len(checks):
        checks *= 2
    return render_template('chart/chart1.html', cats=cats, checks=checks)

@bp.route('/chart2')
def chart2():
    hl = dp_get_image.get_chart2_hl()
    return render_template('chart/chart2.html', hl=hl)

@bp.route('/chart3')
def chart3():
    cats = loc_day_delivery_data.get_cats()
    checks = ["primary", "success", "info", "danger", "warning", "dark"]
    if len(cats) > len(checks):
        checks *= 3
    return render_template('chart/chart3.html', cats=cats, checks=checks, len=len(cats))

@bp.route('/chart4')
def chart4():
    data = order_population_data.get_chart4()
    return render_template('chart/chart4.html',data=data)

@bp.route('/chart5')
def chart5():
    data = order_resident_data.get_chart5()
    addr1 = order_resident_data.get_addr()
    return render_template('chart/chart5.html', data=data, addr1=addr1)

@bp.route('/chart6')
def chart6():
    addr1 = weather_delivery_data.get_addr1()
    addr2 = weather_delivery_data.get_addr2(addr1[0])

    return render_template('chart/chart6.html', addr1=addr1, addr2=addr2)

# 서브페이지 차트
@bp.route('/chart1_sec1', methods=("GET",))
def chart1_sec1():
    wants = request.values.get("wants")
    return lp_get_image.save_img_chart1_sec1(wants)

@bp.route('/chart3_sec1', methods=("GET",))
def chart3_sec1():
    cats = request.values.get("cats").split(",")
    return ldd_get_image.save_img_chart3_sec1(cats)

@bp.route('/chart5_sec1', methods=("GET",))
def chart5_sec1():
    addr = request.values.get("addr")
    return or_get_image.save_img_chart5_sec1(addr)

@bp.route('/chart6_sec1')
def chart6_sec1():
    return wd_get_image.save_img_chart6_sec1()

@bp.route('/chart6_sec2', methods=("GET",))
def chart6_sec2():
    loc = request.values.get("loc")
    addr = request.values.get("addr")
    return wd_get_image.save_img_chart6_sec2(loc, addr)


# 기타 잡
@bp.route('/get_addr2', methods=("GET",))
def get_addr2():
    addr1 = request.values.get("addr1")
    return {"addr2": weather_delivery_data.get_addr2(addr1)}

@bp.route('/get_popular')
def get_popular():
    list = mango_get_data.get_popular_list()
    return {"popular": list}
