# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
import security.huffman as h


# Create your views here.

logged = False
dict = {}


def crypt(code: str):
    bitStream, freqTable = h.Huffman.encodeHuffman(code)
    myTextcoded, length = h.Huffman.bitStream2str(bitStream)
    return freqTable, length, myTextcoded


def index(request):
    return (HttpResponse("Hello World !"))


def homepage(request):
    return (render(request, 'index.html'))


def start(request):
    return (render(request, "login.html"))


def login(request):
    global logged
    global dict
    if request.method == 'GET':
        username = request.GET['name']
        password = request.GET['password']

        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        cur.execute(
            'SELECT COUNT(*) FROM myapp_user WHERE name=? AND password=? ', (username, password))
        result = cur.fetchone()[0]
        if (int(result) != 0):
            cur.execute(
                'SELECT * FROM myapp_user WHERE name=? AND password=? ', (username, password))
            var = cur.fetchone()
            dic = {"nom": var[1], "major": var[4], "status": var[3]}
            dict = {"id": var[0], "name": var[1],
                    "status": var[3], "major": var[4]}
            conn.close()
            logged = True
            return (render(request, 'display.html', {"mydata": dic}))
        else:
            choose = "red"
            conn.close()
            return render(request, "login.html", {"color": choose})

    return (render(request, 'login.html'))


def signin(request):
    return (render(request, 'signin.html'))


def add(request):

    if request.method == 'GET':
        username = request.GET['name']
        Id = request.GET['Id']
        password = request.GET['password']
        major = request.GET.get('major')

        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        cur.execute('SELECT COUNT(*) FROM myapp_user WHERE id=?', (Id,))
        result = cur.fetchone()[0]

        if (int(result) == 0):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cur.execute('INSERT INTO myapp_user VALUES (?,?,?,?,?)',
                        (Id, username, password, "student", major))
            conn.commit()
            conn.close()
            return (render(request, "login.html"))
        else:
            choose = "red"
            conn.close()
            return render(request, "signin.html", {"color": choose})

    return (render(request, 'signin.html'))


def id(request, parametre):
    print(parametre)
    return render(request, 'display.html')


def result(request):
    iq = request.GET.get('iq', None)
    name = request.GET.get('name', None)
    values = request.GET.get('values', None)
    values2 = request.GET.get('values2', None)
    values3 = request.GET.get('values3', None)
    juniorNetworkAdministrator = request.GET.get('jna', None)
    juniorWebProgramer = request.GET.get('jwp', None)
    juniorProgramer = request.GET.get('jp', None)
    print(iq, name, values, values2, values3, juniorNetworkAdministrator,
          juniorWebProgramer, juniorProgramer)


def getPrediction(studentIQ: int, subjectsOutside: list, subjectsIT: list, name: str, hobbies: list) -> str:
    import tensorflow as tf
    import pandas as pd
    import numpy as np
    # Import the model via the load_model function
    model = tf.keras.models.load_model('./model/settings')

    # Declaration of class names
    CLASS_NAMES = {'Junior Network Administrator',
                   'Junior Programmer', 'Junior Web Programmer'}

    variables = {
        "iq": studentIQ,
        "interest_outside_school": [subjectsOutside[0] if subjectsOutside[0] else "''"],
        "interest_outside_school_2": [subjectsOutside[1] if subjectsOutside[1] else "''"],
        "interest_outside_school_3": [subjectsOutside[2] if subjectsOutside[2] else "''"],
        "interest_outside_school_4": [subjectsOutside[3] if subjectsOutside[3] else "''"],
        "favorite_subject_it": [subjectsIT[0] if subjectsIT[0] else "''"],
        "favorite_subject_it_2": [subjectsIT[1] if subjectsIT[1] else "''"],
        "favorite_subject_it_3": [subjectsIT[2] if subjectsIT[2] else "''"],
        "favorite_subject_it_4": [subjectsIT[3] if subjectsIT[3] else "''"],
        "name": name,
        "hobbies": [hobbies[0] if hobbies[0] else "''"],
        "hobbies_2": [hobbies[1] if hobbies[1] else "''"],
        "hobbies_3": [hobbies[2] if hobbies[2] else "''"],
        "hobbies_4": [hobbies[3] if hobbies[3] else "''"],
        "hobbies_5": [hobbies[4] if hobbies[4] else "''"],
        "hobbies_6": [hobbies[5] if hobbies[5] else "''"],
        "hobbies_7": [hobbies[6] if hobbies[6] else "''"],
        "hobbies_8": [hobbies[7] if hobbies[7] else "''"],
        "hobbies_9": [hobbies[8] if hobbies[8] else "''"],
        "junior_network_administrator": 82.8,
        "junior_web_programmer": 76.42,
        "junior_programmer": 80.7,
    }

    input_dict = {name: tf.convert_to_tensor(
        [value]) for name, value in variables.items()}
    prediction = np.argmax(model.predict(input_dict))
    prediction = pd.DataFrame(CLASS_NAMES)[0][prediction]


def result(request):
    studentIQ = request.GET.get('studentIQ', None)
    subjectsOutside = request.GET.get('subjectsoutside', None).split(',')
    subjectsIT = request.GET.get('subjectsIT', None).split(',')
    hobbies = request.GET.get('hobbies', None).split(',')
    name = request.GET['name']

    # ---- MODEL ----#

    return render(request, "result.html")


def profile(request):
    print(logged, dict)
    return (render(request, 'profile.html', {"mydata": dict}))
