from flask import Flask, jsonify, request, render_template, send_file
import datetime
import pyrebase
import xlsxwriter


now = datetime.datetime.now()

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyAwUu-9bNklf0xQWIpqs42fDaMu8ISyDq4",
    "authDomain": "https://student-management-89004.firebaseapp.com/",
    "databaseURL": "https://student-management-89004.firebaseio.com/",
    "storageBucket": "student-management-89004.appspot.com",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


usns = [
        '1DS15EE001', '1DS15EE002', '1DS15EE003', '1DS15EE004', '1DS15EE005', '1DS15EE006', '1DS15EE007',
        '1DS15EE008', '1DS15EE009', '1DS15EE010', '1DS15EE011', '1DS15EE012', '1DS15EE013', '1DS15EE014',
        '1DS15EE015', '1DS15EE016', '1DS15EE017', '1DS15EE018', '1DS15EE019', '1DS15EE020', '1DS15EE021',
        '1DS15EE022', '1DS15EE023', '1DS15EE024', '1DS15EE025', '1DS15EE026', '1DS15EE027', '1DS15EE028',
        '1DS15EE029', '1DS15EE030', '1DS15EE031', '1DS15EE032', '1DS15EE033', '1DS15EE034', '1DS15EE035',
        '1DS15EE036', '1DS15EE037', '1DS15EE038', '1DS15EE039', '1DS15EE040', '1DS15EE041', '1DS15EE042',
        '1DS15EE043', '1DS15EE044', '1DS15EE045', '1DS15EE046', '1DS15EE047', '1DS15EE048', '1DS15EE049',
        '1DS15EE050', '1DS15EE051', '1DS15EE052', '1DS15EE053', '1DS15EE054', '1DS15EE055', '1DS15EE056',
        '1DS15EE058', '1DS15EE059', '1DS15EE060', '1DS15EE061', '1DS15EE062', '1DS15EE063', '1DS15EE064',
        '1DS15EE065', '1DS15EE066', '1DS15EE067', '1DS15EE068', '1DS15EE069', '1DS15EE070', '1DS15EE071',
        '1DS15EE072', '1DS15EE073', '1DS15EE074', '1DS15EE075', '1DS15EE076', '1DS15EE077', '1DS15EE078',
        '1DS15EE079', '1DS15EE080', '1DS15EE081', '1DS15EE082', '1DS15EE083', '1DS15EE084', '1DS15EE085',
        '1DS15EE086', '1DS15EE087', '1DS15EE088', '1DS15EE089', '1DS15EE090', '1DS15EE091', '1DS15EE092',
        '1DS15EE093', '1DS15EE094', '1DS15EE095', '1DS15EE096', '1DS15EE097', '1DS15EE098', '1DS15EE099',
        '1DS15EE100', '1DS15EE101'
        ]

usn = []
sub_name = []
date = []
present = []
marks = []

subjects = [
        {
            'id': 1,
            'name': 'Network Analysis'
        },
        {
            'id': 2,
            'name': 'Logic Design'
        },
        {
            'id': 3,
            'name': 'Analog Electronic Circuits'
        },
        {
            'id': 4,
            'name': 'Mathematics'
        },
        {
            'id': 5,
            'name': 'Electrical Machines'
        },
        {
            'id': 6,
            'name': 'Electrical Instruments'
        },
        {
            'id': 7,
            'name': 'AEC LAB'
        },
        {
            'id': 8,
            'name': 'LD LAB'
        }
    ]

details = []

data = []
obj = {}

#firebase = firebase.FirebaseApplication('https://student-management-89004.firebaseio.com/', None)
#result = firebase.get('/details', None)


def fetch_data():
    received = db.child("details").get()
    for rec_data in received.each():
        key_main = rec_data.key()
        val_main = rec_data.val()


        for _k, _v in val_main.iteritems():
            if _k in usn:
                pass
            else:
                usn.append(_k)


            for _k, _v in _v.iteritems():
                sub_name.append(_k)

                for _k, _v in _v.iteritems():
                    if _k == 'marks':
                        marks.append(_v)
                    else:
                        date.append(_k)
                        present.append(_v)



def fetch_attendance(usn, sub):
    rec = db.child("details").get()
    global present
    present = []
    for _data in rec.each():
        _key = _data.key()
        _val = _data.val()

        for _k, _v in _val.iteritems():
            if _k == usn:
                for _k, _v in _v.iteritems():
                    if _k == sub:
                        for _k, _v in _v.iteritems():
                            if _k == "marks":
                                pass
                            else:
                                present.append(_v)





@app.route('/test')
def test():
    fetch_attendance("1DS15EE3", "Logic Design")
    y_count = 0
    n_count = 0

    print '----------'
    for u in usn:
        print 'usn'
        print u

    print '----------'
    for s in sub_name:
        print 'sub'
        print s

    print '----------'
    for d in date:
        print 'date'
        print d

    print '----------'
    for p in present:
        print 'present'
        if p['present'] == 'Y':
            y_count += 1
        elif p['present'] == 'N':
            n_count += 1
    print y_count
    print n_count

    print '----------'
    for m in marks:
        print 'marks'
        print m
    print '----------'
    return "processed"


@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/sheet')
def export():

    workbook = xlsxwriter.Workbook('data.xlsx')

    worksheet = workbook.add_worksheet()
    '''worksheet.write('A1', 'Sl. No.')
    worksheet.write('B1', 'USN')
    worksheet.write('C1', 'Sub1')
    worksheet.write('D1', 'Sub2')'''

    row = 0
    col = 2

    worksheet.write(row, 0, 'Sl. No.')
    worksheet.write(row, 1, 'USN')



    for i in range(len(subjects)):
        sub = subjects[i]
        for k, v in sub.iteritems():
            if k == 'name':
                worksheet.write(row, col, v)
                col += 1

    for i in range(len(usns)):
        usn = usns[i]
        worksheet.write(row+1, 0, i+1)
        worksheet.write(row+1, 1, usn)
        row += 1





    workbook.close()


    return send_file('data.xlsx', attachment_filename='data.xlsx')

@app.route('/att')
def get_att():
    usn = request.args.get('usn')
    subject = request.args.get('sub')
    fetch_attendance(usn, subject)
    y_count = 0
    n_count = 0
    for p in present:
        print 'present'
        if p['present'] == 'Y':
            y_count += 1
        elif p['present'] == 'N':
            n_count += 1
    print y_count
    print n_count

    total = y_count+n_count
    try:
        _pre = (y_count/float(total)) * 100
        _abs = (n_count/float(total)) * 100
    except Exception as e:
        print "Not Found in database"
        _pre = 0
        _abs = 0

    print _pre
    print _abs


    return render_template('att.html', present=_pre, absent=_abs, usn=usn, sub=subject,
                           yes=y_count, no=n_count, total=total)



@app.route('/sub', methods=['POST', 'GET'])
def save_sub():
    found = False
    sub_code = int(request.args.get('code'))
    usn = request.args.get('usn')
    marks = request.args.get('marks')
    present = request.args.get('present')
    subject = ''
    for sub in subjects:
        if sub['id'] == sub_code:
            subject = sub['name']
    date = str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ':' + str(now.hour)
    usn_details = {
            subject: {
                date: {
                    "present": present
                },
                "marks": marks
            }
    }

    detail = {
        usn: usn_details
    }


    if len(details) > 0:
        for i in range(len(details)):
            print details[i]
            if usn in details[i]:
                details[i][usn].update(usn_details)
                found = True
        for j in range(len(details)):
            if not found:
                details.append(detail)
                found = False
                break
    else:
        details.append(detail)


    print details
    db.child("details").set(details)
    return jsonify({'details': details})


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80, debug=True)
    #app.run()