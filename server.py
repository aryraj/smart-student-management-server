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

usns = ['1DS15EE001', '1DS15EE002', '1DS15EE003', '1DS15EE004', '1DS15EE005', '1DS15EE006', '1DS15EE007',
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

