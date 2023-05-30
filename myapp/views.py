# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
import security.huffman as h

# Create your views here.

def crypt(code : str):
    bitStream,freqTable  = h.Huffman.encodeHuffman(code)
    myTextcoded, length = h.Huffman.bitStream2str(bitStream)
    return freqTable, length, myTextcoded

def index(request):
    return (HttpResponse("Hello World !"))

def homepage(request):
    return(render(request,'index.html'))

def start(request):
    return (render( request,"login.html"))

def login(request):
    if request.method == 'GET':
        username = request.GET['name']
        password = request.GET['password']
    
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        
        cur.execute('SELECT COUNT(*) FROM myapp_user WHERE name=? AND password=? ',(username,password))
        result = cur.fetchone()[0]
        if (int(result)!=0):
            cur.execute('SELECT id FROM myapp_user WHERE name=? AND password=? ',(username,password))
            result = cur.fetchone()[0]
            conn.close()
            mydata = {"freqTable" : "", "lenght": "", "id": ""}
            result= str(result) + "," +username +password
            mydata['freqTable'], mydata['lenght'], mydata['id'] = crypt(result) # type: ignore
            return (render(request, 'display.html', {"mydata" : mydata}))
        else:
            choose = "red"
            conn.close()
            return render(request, "login.html", {"color": choose})
        
    return(render(request,'login.html'))

def signin(request):
    return(render(request,'signin.html'))

def add(request):
    
    if request.method == 'GET':
        username = request.GET['name']
        Id = request.GET['Id']
        password = request.GET['password']
        
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        
        cur.execute('SELECT COUNT(*) FROM myapp_user WHERE id=?',(Id,))
        result = cur.fetchone()[0]
        
        if (int(result)==0):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cur.execute('INSERT INTO myapp_user VALUES (?,?,?,?)',(Id,username,password,"student"))
            conn.commit()
            conn.close()
            return (render(request,"login.html"))
        else : 
            choose = "red"
            conn.close()
            return render(request, "signin.html", {"color": choose})
        
    return(render(request,'signin.html'))
    