import pymysql
from datetime import datetime


conn = pymysql.connect(host='192.168.0.13.',
                       user='park',
                       password='pi',
                       db='testDB',
                       charset='utf8')
sqsl ="INSERT INTO garbage(metal, plastic, trash, unknown, time)
VALUES (%s, %s,%s,%s);"

def add_data(metal, plastic, trash, unknown):
    now = datetime.now()
    conn.cursor()
    dt= now.time()
    dt = str(dt)
    dt = dt[0:10]
    conn.cursor().execute(sql, (metal,plastic,trash,unknown,dt))
    conn.commit()
    conn.close()
