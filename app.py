from flask import Flask, render_template
import pymysql
import re

app = Flask(__name__)

conn = pymysql.connect(host='192.168.0.13',
                        user = 'park',
                        passwd='pi',
                        db='testDB',
                        charset='utf8')


def sensor_receive():
    global metal, plastic, trash, unknown, timeAmount
    with conn.cursor() as cur:
        sql = "select * from garbage"
        cur.execute(sql)
        for row in cur.fetchall():
            metal = row[0]
            plastic = row[1]
            trash = row[2]
            unknown = row[3]
            clock = re.sub(r'[^0-9]', '', row[4])
            print(type(clock))
            print(clock)
            print(row)




@app.route('/', methods = ['POST', "GET"])
def hello():
    sensor_receive()
    amount = plastic + metal + trash + unknown
    print(amount)
    pc_pla = int((plastic / amount) * 100)  # amount가 0이면 우짜게?
    pc_met = int((metal / amount) * 100)
    pc_tra = int((trash / amount) * 100)
    pc_unk = int((unknown / amount) * 100)
    return render_template('index.html', amount = amount,
                           pc_pla=pc_pla, pc_met=pc_met, pc_unk=pc_unk, pc_tra=pc_tra)


@app.route('/chart', methods = ['POST', "GET"])
def chart():
    # Total amount Chart
    sensor_receive()
    amount = plastic + metal + trash + unknown
    # Bar chart

    # Pi chart
    pc_pla = int((plastic/amount)*100) # amount가 0이면 우짜게?
    pc_met = int((metal/amount)*100)
    pc_tra = int((trash/amount)*100)
    pc_unk = int((unknown/amount)*100)
    print(pc_pla, pc_met, pc_tra, pc_unk)
    return render_template('charts.html',
                           plastic=plastic, metal=metal, trash=trash, unknown = unknown,
                           pc_pla = pc_pla, pc_met = pc_met, pc_unk = pc_unk, pc_tra=pc_tra)

@app.route('/us')
def us():
    return render_template('aboutUs.html')

@app.route('/rc')
def rc():
    return render_template('RemoteControl.html')

if __name__ == '__main__':
    app.debug = True
    #app.run()
    app.run(host='192.168.0.4')
    #app.run(host='0.0.0.0')