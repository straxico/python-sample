import os
from flask import Flask
import time
import random
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
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Got command: %s' % command)
    
    if command == 'roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == 'time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))


    mss = command
    
    mss=mss.replace('/', ',')
    mss=mss.replace('.', ',')
    mss=mss.replace('-', ',')
    mss=mss.split(',')
    now =JalaliDatetime.now()
    old=JalaliDatetime(int(mss[0]),int(mss[1]),int(mss[2])).todate() 
    dif = [100,200,222,300,333,400,444,500,555,600,666,700,777,800,888,900,999,1000,1111,2000,2222,3000,3333,4000,4444,5000,5555,6000,6666,7000,7777,8000,8228,8888,9999,10000,11111]
    i=0
    ss=''
    for x in dif:
        dif1=datetime.timedelta(x)
        date=old+dif1
        jdate=JalaliDatetime(date)
        if (jdate>now and i<5):
            ss= ss + '\n' + str(jdate.strftime('%A %D %B %N')) +'میشی '+str(dif1.days) +"روزه "
            i=i+1

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
