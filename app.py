# -*- coding: utf-8 -*-
import os
from flask import Flask
import time
import datetime
import telepot
from khayyam import JalaliDatetime



import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

app = Flask(__name__)

@app.route('/')
def hello():
    return 'strix bot'

def handle(msg):
 content_type, chat_type, chat_id = telepot.glance(msg)
 if content_type == 'text':
    command = msg['text']
    print ('Got command: %s' % command)
    mss = command
    mss=mss.replace('/', ',')
    mss=mss.replace('.', ',')
    mss=mss.replace('-', ',')
    mss=mss.split(',')
    now =JalaliDatetime.now()
    if len(mss)<3 :
         if command == 'Time':
             ss=str(datetime.datetime.now())
         elif command == '/help':
             sss= 'سلام واسه استفاده بايد تاريخ رو با يکي از فرمت هاي زير وارد کني' +'\n'+'1364/3/27'+'\n'+'1382-3-27'+'\n'+'1373.1.15'+'\n'+'1373,4,5'
             ss= str(sss)
         elif command == '/start':
            ss=str("خیلی خوش اومدی لطفا یه تاریخ وارد کن")
            
         elif command == 'ممنون':
            ss=str("خواهش میکنم مهربون .. قابلی نداشت ")
         elif command == 'احمق':
             ss=str("خودتی")
         else :
           ss='اگه میشه تاریخ رو اینجوری وارد کن تا من بتونم بخونمش' + '\t' + '1372.11.5'
    else:
     old=JalaliDatetime(int(mss[0]),int(mss[1]),int(mss[2]))
     dif = [100,200,222,300,333,400,444,500,555,600,666,700,777,800,888,900,999,1000,1111,2000,2222,3000,3333,4000,4444,5000,5555,6000,6666,7000,7777,8000,8228,8888,9000,9009,9999,10000,11111,12000,13000,14000,15000,16000,17000,18000,19000,20000,21000,22000,22222,23000,24000,25000,26000,27000]
     i=0
     d=(now-old).days
     ss='سلام امروز ' +str(d)+ ' روزه هستی '
     for x in dif:
        dif1=datetime.timedelta(x)
        date=old+dif1
        jdate=JalaliDatetime(date)
        if (jdate>now and i<10):
             ss= ss + '\n' + str(jdate.strftime('%A %D %B %N')) +  ' میشی '+str(dif1.days) + " روزه "
             i=i+1
     ss= ss +'\n' +'\n' + 'مواظب خوبیات باش' +" @strixdaybot "
    print(ss)
    bot.sendMessage(chat_id, text= ss )

bot = telepot.Bot('375977039:AAEGag8W43sQmo61KmBnvtVXFOsVAP7PIwk')
bot.message_loop(handle)
print ('I am listening ...')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    

while 1:
    time.sleep(10)
