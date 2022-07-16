import flask,os
import pandas as pd
from flask import render_template,request
import time,datetime
from flask import app

main_dir=os.getcwd()
data=pd.read_csv('dir.csv')
date=pd.read_csv('date.csv')
a=flask.Flask(__name__)

def finder(docu,chdir=False,type=False):
    di=os.getcwd()
    di=di.replace('/templates','')
    for b,c in data.iterrows():
        for d in c.iloc[0].split(','):
            if d in docu:
                if chdir:
                    os.chdir(di+c.iloc[1]) 
                else:
                    return di+c.iloc[1]
                if type:
                    return c.iloc[2]
                
                
@a.route(r'/')
def home():
    di=os.getcwd()
    di=di.replace('/templates','')
    di+='/static/video'
    li=os.listdir(di)
    return render_template('home.html',vedio=li)

@a.route('/upload')
def upload():
    return render_template('upload.html')

@a.route('/upload',methods=['post'])
def uploaded():
    file_=request.files['file1']
    direc=os.getcwd()
    typ=finder(file_.filename,True,True)
    file_.save(file_.filename)
    if 'docu' in typ:
        typ=file_.filename[(file_.filename).find('.')+1:]
    date.loc[len(date)]=[file_.filename,datetime.datetime.now(),typ]
    date.to_csv(main_dir+'/date.csv',index=False)
    os.chdir(direc)
    return home()

@a.route(r'/play/<video>')
def player(video):
    di=finder(video)
    if video in os.listdir(di):
        a=os.listdir(di)
        a.remove(video)
        return render_template('player.html',main='..'+di[di.find('/static'):]+video,vedo=a)

@a.route('/pdf/<name>')
def showpdf(name):
    return render_template('read.html',doc=name)
@a.route('/docwin')

def showdoc():
    di=os.getcwd()
    di=di.replace('/templates','')
    di+='/static/Doc'
    li=os.listdir(di)
    return render_template('docwin.html',given=li)

try:
    a.run(host='192.168.43.189')

except:
    a.run()
