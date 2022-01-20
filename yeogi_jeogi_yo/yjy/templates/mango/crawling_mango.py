#-*-coding:utf-8-*-
import cx_Oracle as oracle
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import time
from selenium import webdriver

# 경로 수정 필수!
driver = webdriver.Chrome('D:\project2\yeogi_jeogi_yo\yjy\static\chromedriver')

driver.get('https://www.mangoplate.com/search/배달')
time.sleep(5)

url = 'https://www.mangoplate.com/search/delivery'
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

title = soup.find('h2', 'title').text.strip()
point = soup.find('strong', 'point search_point').text.strip()
address = soup.find(class_='etc').text

rankL = []
nameL = []
pointL = []
addressL = []
sectorsL = []

count = 0
rank = 0

list_soup = soup.find_all('div', 'info')
print("[MANGO] start parsing")

for item in list_soup:
    count +=1
    if (count > 20): break
    rank = count

    name = ''
    try: name= item.find('h2', 'title').text.replace(" ","")
    except: name=''

    point = ''
    try: point = item.find('strong', 'point search_point').text.strip()
    except: point=''

    address = ''
    sectors = ''
    try: temp = item.find('p', 'etc').text; address = temp.split('-')[0].rstrip(); sectors = temp.split('-')[1].lstrip()
    except: address=''; sectors = ''

    rankL.append(rank)
    nameL.append(name)
    pointL.append(point)
    addressL.append(address)
    sectorsL.append(sectors)

print("[MANGO] data to csv file")

resultDict = dict( Rank = rankL,
                   Delivery = nameL,
                   Point = pointL,
                   Address = addressL,
                   Secors = sectorsL)

dt = datetime.datetime.now()
fName = f"yjy/static/csv/Mango_{dt.year}_{dt.month}_{dt.day}" + '.csv'
df = pd.DataFrame(resultDict)

df.to_csv(fName, sep=',', encoding='utf-8-sig')

df = pd.read_csv(fName,index_col=0)
df.head()

# DB정보 수정 필수!
db = oracle.connect(user="유저명", password="비밀번호", dsn="localhost")
cursor = db.cursor()
print("[MANGO] DB connected")

print('[MANGO] Droping mango table if exists............')
cursor.execute("BEGIN EXECUTE IMMEDIATE 'DROP TABLE mango'; EXCEPTION WHEN OTHERS THEN NULL; END;")


print('[MANGO] Creating table mango...')
cursor.execute("CREATE TABLE mango (rank number NOT NUll, name varchar2(100) NOT NUll, point number NOT NUll, address varchar2(100) NOT NUll, sectors varchar2(100) NOT NUll)")
print("[MANGO] created")

print("[MANGO] insert...")
for i, row in df.iterrows():
    sql = "INSERT INTO mango(rank,name,point,address,sectors) VALUES(:1,:2,:3,:4,:5)"
    cursor.execute(sql, tuple(row))

print("[MANGO] inserted")

db.commit()
print("[MANGO] commited")

cursor.close()
db.close()
