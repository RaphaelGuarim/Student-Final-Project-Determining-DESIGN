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


def getPrediction(studentIQ: int, subjectsOutside: list, subjectsIT: list, name: str, hobbies: list, juniorNetworkAdministrator: int,
                  juniorWebProgramer: int, juniorProgramer: int) -> str:
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
        "interest_outside_school": subjectsOutside[0],
        "interest_outside_school_2": subjectsOutside[1],
        "interest_outside_school_3": subjectsOutside[2],
        "interest_outside_school_4": subjectsOutside[3],
        "favorite_subject_it": subjectsIT[0],
        "favorite_subject_it_2": subjectsIT[1],
        "favorite_subject_it_3": subjectsIT[2],
        "favorite_subject_it_4": subjectsIT[3],
        "name": name,
        "hobbies": hobbies[0],
        "hobbies_2": hobbies[1],
        "hobbies_3": hobbies[2],
        "hobbies_4": hobbies[3],
        "hobbies_5": hobbies[4],
        "hobbies_6": hobbies[5],
        "hobbies_7": hobbies[6],
        "hobbies_8": hobbies[7],
        "hobbies_9": hobbies[8],
        "junior_network_administrator": juniorNetworkAdministrator,
        "junior_web_programmer": juniorWebProgramer,
        "junior_programmer": juniorProgramer,
    }

    input_dict = {name: tf.convert_to_tensor(
        [value]) for name, value in variables.items()}
    prediction = np.argmax(model.predict(input_dict))
    prediction = pd.DataFrame(CLASS_NAMES)[0][prediction]


def result(request):
    studentIQ = int(request.GET.get('studentIQ', None))

    subjectsOutside = ['', '', '', '']
    subjectsOutsideRAW = request.GET.get('subjectsOutside', None).split(',')
    for i in range(len(subjectsOutsideRAW)):
        subjectsOutside[i] = subjectsOutsideRAW[i]

    subjectsIT = ['', '', '', '']
    subjectsITRAW = request.GET.get('subjectsIT', None).split(',')
    for i in range(len(subjectsITRAW)):
        subjectsIT[i] = subjectsITRAW[i]

    hobbies = ['', '', '', '', '', '', '', '', '']
    hobbiesRAW = request.GET.get('hobbies', None).split(',')
    for i in range(len(hobbiesRAW)):
        subjectsIT[i] = hobbiesRAW[i]

    name = request.GET['name']
    juniorNetworkAdministrator = int(request.GET.get('jna', None))
    juniorWebProgramer = int(request.GET.get('jwp', None))
    juniorProgramer = int(request.GET.get('jp', None))

    # ---- MODEL ----#
    prediction = getPrediction(studentIQ, subjectsOutside, subjectsIT, name, hobbies, juniorNetworkAdministrator,
                               juniorWebProgramer, juniorProgramer)
    return render(request, "result.html")


def profile(request):
    print(logged, dict)
    return (render(request, 'profile.html', {"mydata": dict}))
